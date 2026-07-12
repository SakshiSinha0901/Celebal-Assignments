"""Command-line reporting tool for the e-commerce analytics database."""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

from tabulate import tabulate

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "database" / "ecommerce_analytics.db"

REPORTS = {
    "revenue": """
        SELECT strftime('%Y-%m', o.order_date) AS month,
               ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
        FROM orders o JOIN order_items oi ON oi.order_id = o.order_id
        WHERE o.order_status NOT IN ('Cancelled', 'Returned')
        GROUP BY month ORDER BY month
    """,
    "top_customers": """
        SELECT c.customer_id, c.customer_name,
               ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS lifetime_value,
               COUNT(DISTINCT o.order_id) AS orders
        FROM customers c
        JOIN orders o ON o.customer_id = c.customer_id
        JOIN order_items oi ON oi.order_id = o.order_id
        WHERE o.order_status NOT IN ('Cancelled', 'Returned')
        GROUP BY c.customer_id, c.customer_name
        ORDER BY lifetime_value DESC LIMIT :limit
    """,
    "top_products": """
        SELECT p.product_name, p.category, SUM(oi.quantity) AS quantity_sold,
               ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
        FROM products p
        JOIN order_items oi ON oi.product_id = p.product_id
        JOIN orders o ON o.order_id = oi.order_id
        WHERE o.order_status NOT IN ('Cancelled', 'Returned')
        GROUP BY p.product_id, p.product_name, p.category
        ORDER BY revenue DESC LIMIT :limit
    """,
    "retention": """
        WITH customer_orders AS (
            SELECT DISTINCT customer_id, strftime('%Y-%m', order_date) AS activity_month
            FROM orders WHERE order_status NOT IN ('Cancelled', 'Returned')
        ), first_purchase AS (
            SELECT customer_id, MIN(activity_month) AS cohort_month
            FROM customer_orders GROUP BY customer_id
        ), cohort_activity AS (
            SELECT co.customer_id, fp.cohort_month, co.activity_month,
                   ((CAST(substr(co.activity_month,1,4) AS INTEGER)-CAST(substr(fp.cohort_month,1,4) AS INTEGER))*12
                   +CAST(substr(co.activity_month,6,2) AS INTEGER)-CAST(substr(fp.cohort_month,6,2) AS INTEGER)) AS month_number
            FROM customer_orders co JOIN first_purchase fp ON fp.customer_id=co.customer_id
        ), cohort_size AS (
            SELECT cohort_month, COUNT(DISTINCT customer_id) AS size
            FROM first_purchase GROUP BY cohort_month
        )
        SELECT ca.cohort_month, ca.month_number, cs.size AS cohort_size,
               COUNT(DISTINCT ca.customer_id) AS retained_customers,
               ROUND(COUNT(DISTINCT ca.customer_id)*100.0/cs.size, 2) AS retention_percent
        FROM cohort_activity ca JOIN cohort_size cs ON cs.cohort_month=ca.cohort_month
        GROUP BY ca.cohort_month, ca.month_number, cs.size
        ORDER BY ca.cohort_month DESC, ca.month_number LIMIT :limit
    """,
    "segments": """
        WITH metrics AS (
            SELECT c.customer_id, c.customer_name,
                   COUNT(DISTINCT o.order_id) AS frequency,
                   COALESCE(SUM(oi.quantity*oi.unit_price*(1-oi.discount)),0) AS monetary
            FROM customers c
            LEFT JOIN orders o ON o.customer_id=c.customer_id AND o.order_status NOT IN ('Cancelled','Returned')
            LEFT JOIN order_items oi ON oi.order_id=o.order_id
            GROUP BY c.customer_id, c.customer_name
        )
        SELECT customer_id, customer_name, frequency, ROUND(monetary,2) AS spend,
               CASE WHEN frequency<=1 THEN 'One-time' WHEN frequency<=4 THEN 'Occasional' ELSE 'Loyal' END AS frequency_segment,
               CASE WHEN monetary<10000 THEN 'Low' WHEN monetary<50000 THEN 'Medium' ELSE 'High' END AS spend_tier
        FROM metrics ORDER BY monetary DESC LIMIT :limit
    """,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run e-commerce analytics reports.")
    parser.add_argument("--report", required=True, choices=sorted(REPORTS))
    parser.add_argument("--limit", type=int, default=15, help="Maximum rows for limited reports (1-100).")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite database path.")
    parser.add_argument("--format", choices=["table", "csv"], default="table")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not 1 <= args.limit <= 100:
        print("Error: --limit must be between 1 and 100.", file=sys.stderr)
        return 2
    if not args.db.exists():
        print(f"Error: database not found at {args.db}", file=sys.stderr)
        print("Run: python scripts/load_database.py", file=sys.stderr)
        return 1

    try:
        with sqlite3.connect(args.db) as conn:
            cursor = conn.execute(REPORTS[args.report], {"limit": args.limit})
            rows = cursor.fetchall()
            headers = [column[0] for column in cursor.description]
    except sqlite3.Error as exc:
        print(f"Database error: {exc}", file=sys.stderr)
        return 1

    if not rows:
        print(f"No data found for report '{args.report}'.")
        return 0

    if args.format == "csv":
        print(",".join(headers))
        for row in rows:
            print(",".join(str(value) for value in row))
    else:
        print(f"\nReport: {args.report.replace('_', ' ').title()}\n")
        print(tabulate(rows, headers=headers, tablefmt="github", floatfmt=",.2f"))
        print(f"\nRows displayed: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
