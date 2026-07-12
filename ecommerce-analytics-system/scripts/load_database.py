"""Create the SQLite database and load all cleaned CSV files."""
from __future__ import annotations

import sqlite3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "database" / "ecommerce_analytics.db"
CLEAN_DIR = ROOT / "data" / "cleaned"
SCHEMA_PATH = ROOT / "sql" / "schema.sql"

TABLE_FILES = {
    "customers": "customers_clean.csv",
    "products": "products_clean.csv",
    "orders": "orders_clean.csv",
    "order_items": "order_items_clean.csv",
}


def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        for table, filename in TABLE_FILES.items():
            frame = pd.read_csv(CLEAN_DIR / filename)
            frame.to_sql(table, conn, if_exists="append", index=False)
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"Loaded {table:<12} rows={count:>5}")

        broken_orders = conn.execute("""
            SELECT COUNT(*) FROM orders o
            LEFT JOIN customers c ON c.customer_id = o.customer_id
            WHERE c.customer_id IS NULL
        """).fetchone()[0]
        broken_items = conn.execute("""
            SELECT COUNT(*) FROM order_items oi
            LEFT JOIN orders o ON o.order_id = oi.order_id
            LEFT JOIN products p ON p.product_id = oi.product_id
            WHERE o.order_id IS NULL OR p.product_id IS NULL
        """).fetchone()[0]
        print(f"Broken order references: {broken_orders}")
        print(f"Broken item references : {broken_items}")
        if broken_orders or broken_items:
            raise RuntimeError("Referential integrity verification failed.")
    print(f"\nSQLite database created at: {DB_PATH}")


if __name__ == "__main__":
    main()
