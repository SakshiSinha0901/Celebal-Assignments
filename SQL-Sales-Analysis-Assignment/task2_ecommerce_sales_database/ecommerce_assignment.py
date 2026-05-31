import os
import sqlite3
import pandas as pd

DB_FILE = "ecommerce.db"
SETUP_SQL_FILE = "ecommerce_setup.sql"
QUERIES_SQL_FILE = "ecommerce_queries.sql"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

with open(SETUP_SQL_FILE, "r", encoding="utf-8") as file:
    setup_sql = file.read()

cursor.executescript(setup_sql)
conn.commit()

print("Database created and sample data inserted successfully.")

def run_query(query):
    return pd.read_sql_query(query, conn)

queries = {
    "q1_all_customers": """
    SELECT *
    FROM customers;
    """,

    "q2_customer_names_city": """
    SELECT first_name, last_name, city
    FROM customers;
    """,

    "q3_unique_product_categories": """
    SELECT DISTINCT category
    FROM products;
    """,

    "q7_delivered_orders": """
    SELECT *
    FROM orders
    WHERE status = 'Delivered';
    """,

    "q8_electronics_above_2000": """
    SELECT *
    FROM products
    WHERE category = 'Electronics'
      AND unit_price > 2000;
    """,

    "q9_maharashtra_customers_2024": """
    SELECT *
    FROM customers
    WHERE join_date >= '2024-01-01'
      AND join_date < '2025-01-01'
      AND state = 'Maharashtra';
    """,

    "q10_orders_between_dates_not_cancelled": """
    SELECT *
    FROM orders
    WHERE order_date BETWEEN '2024-08-10' AND '2024-08-25'
      AND status <> 'Cancelled';
    """,

    "q11_index_benefit_sample_query": """
    SELECT *
    FROM orders
    WHERE order_date BETWEEN '2024-08-01' AND '2024-08-20';
    """,

    "q12_sargable_join_date_query": """
    SELECT *
    FROM customers
    WHERE join_date >= '2024-01-01'
      AND join_date < '2025-01-01';
    """,

    "q13_total_orders": """
    SELECT COUNT(*) AS total_orders
    FROM orders;
    """,

    "q14_total_revenue_delivered": """
    SELECT SUM(total_amount) AS delivered_revenue
    FROM orders
    WHERE status = 'Delivered';
    """,

    "q15_average_unit_price_by_category": """
    SELECT category,
           ROUND(AVG(unit_price), 2) AS average_unit_price
    FROM products
    GROUP BY category;
    """,

    "q16_order_count_revenue_by_status": """
    SELECT status,
           COUNT(*) AS order_count,
           SUM(total_amount) AS total_revenue
    FROM orders
    GROUP BY status
    ORDER BY total_revenue DESC;
    """,

    "q17_max_min_product_price_by_category": """
    SELECT category,
           MAX(unit_price) AS most_expensive_product_price,
           MIN(unit_price) AS cheapest_product_price
    FROM products
    GROUP BY category;
    """,

    "q18_categories_avg_price_above_2000": """
    SELECT category,
           ROUND(AVG(unit_price), 2) AS average_unit_price
    FROM products
    GROUP BY category
    HAVING AVG(unit_price) > 2000;
    """,

    "q19_inner_join_orders_customers": """
    SELECT o.order_id,
           o.order_date,
           c.first_name,
           c.last_name,
           o.total_amount
    FROM orders o
    INNER JOIN customers c
        ON o.customer_id = c.customer_id;
    """,

    "q20_left_join_customers_orders": """
    SELECT c.customer_id,
           c.first_name,
           c.last_name,
           o.order_id,
           o.order_date,
           o.total_amount
    FROM customers c
    LEFT JOIN orders o
        ON c.customer_id = o.customer_id;
    """,

    "q21_three_table_join_order_items_products": """
    SELECT oi.order_id,
           p.product_name,
           oi.quantity,
           oi.unit_price,
           oi.discount_pct
    FROM order_items oi
    INNER JOIN orders o
        ON oi.order_id = o.order_id
    INNER JOIN products p
        ON oi.product_id = p.product_id;
    """,

    "q24_case_price_tiers": """
    SELECT product_name,
           unit_price,
           CASE
               WHEN unit_price < 1000 THEN 'Budget'
               WHEN unit_price BETWEEN 1000 AND 3000 THEN 'Mid-Range'
               WHEN unit_price > 3000 THEN 'Premium'
           END AS price_tier
    FROM products;
    """,

    "q25_delivered_vs_not_delivered": """
    SELECT
        SUM(CASE WHEN status = 'Delivered' THEN 1 ELSE 0 END) AS delivered_orders,
        SUM(CASE WHEN status <> 'Delivered' THEN 1 ELSE 0 END) AS not_delivered_orders
    FROM orders;
    """,

    "validation_customers_count": """
    SELECT COUNT(*) AS total_customers
    FROM customers;
    """,

    "validation_products_count": """
    SELECT COUNT(*) AS total_products
    FROM products;
    """,

    "validation_orders_count": """
    SELECT COUNT(*) AS total_orders
    FROM orders;
    """,

    "validation_order_items_count": """
    SELECT COUNT(*) AS total_order_items
    FROM order_items;
    """
}

combined_md = "# E-Commerce SQL Query Results\n\n"

for name, query in queries.items():
    result = run_query(query)

    csv_path = os.path.join(OUTPUT_DIR, f"{name}.csv")
    result.to_csv(csv_path, index=False)

    combined_md += f"## {name}\n\n"
    combined_md += result.to_string(index=False)
    combined_md += "\n\n"

with open(os.path.join(OUTPUT_DIR, "query_results.md"), "w", encoding="utf-8") as file:
    file.write(combined_md)

print("Query outputs saved successfully.")

try:
    cursor.execute("""
    INSERT INTO products VALUES
    (209, 'Test Product', 'Electronics', 'TestBrand', -50.00, 10);
    """)
    conn.commit()

except Exception as error:
    conn.rollback()

    with open(os.path.join(OUTPUT_DIR, "q6_constraint_test.txt"), "w", encoding="utf-8") as file:
        file.write("Q6 Constraint Test\n\n")
        file.write("Query tried:\n")
        file.write("INSERT INTO products VALUES (209, 'Test Product', 'Electronics', 'TestBrand', -50.00, 10);\n\n")
        file.write("Expected result:\n")
        file.write("The insert failed because unit_price has CHECK (unit_price > 0).\n\n")
        file.write("Actual error:\n")
        file.write(str(error))

print("Q6 constraint test saved successfully.")

conn.close()

print("Task 2 completed successfully.")