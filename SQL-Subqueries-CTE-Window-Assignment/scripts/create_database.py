import sqlite3
import pandas as pd
from pathlib import Path

# This gives the main assignment folder path
BASE_DIR = Path(__file__).resolve().parent.parent

# CSV file path
DATA_PATH = BASE_DIR / "data" / "superstore.csv"

# SQLite database file path
DB_PATH = BASE_DIR / "superstore_sales.db"

# SQL file path
SQL_PATH = BASE_DIR / "superstore_analysis.sql"

# Folder where query result CSV files will be saved
RESULTS_DIR = BASE_DIR / "results"

# Create results folder if it does not already exist
RESULTS_DIR.mkdir(exist_ok=True)


def clean_column_names(df):
    """
    This function makes column names easier to use in SQL.
    Example: 'Customer Name' becomes 'customer_name'.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df


def main():
    print("Loading Superstore dataset...")

    # Read the Superstore CSV file
    # latin1 encoding is used because some product names may contain special characters
    df = pd.read_csv(DATA_PATH, encoding="latin1")

    # Clean column names before creating database table
    df = clean_column_names(df)

    # These columns should behave like numbers in SQL queries
    numeric_columns = ["sales", "quantity", "discount", "profit"]

    # Convert selected columns into numeric values
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Create connection with SQLite database
    # If the database does not exist, it will be created automatically
    conn = sqlite3.connect(DB_PATH)

    print("Creating superstore_raw table...")

    # Save the complete CSV data into a raw table
    df.to_sql("superstore_raw", conn, if_exists="replace", index=False)

    print("Running SQL script...")

    # Read the SQL file that contains table creation and analysis queries
    with open(SQL_PATH, "r", encoding="utf-8") as file:
        sql_script = file.read()

    # Execute all SQL statements written in the SQL file
    conn.executescript(sql_script)

    # These all are the important queries whose results we want to save as CSV files
    queries_to_export = {
        "01_above_average_sales.csv": """
            SELECT
                order_id,
                customer_id,
                customer_name,
                product_name,
                sales
            FROM superstore_raw
            WHERE sales > (SELECT AVG(sales) FROM superstore_raw)
            ORDER BY sales DESC;
        """,

        "02_highest_order_per_customer.csv": """
            SELECT
                customer_id,
                customer_name,
                order_id,
                product_name,
                sales
            FROM superstore_raw s1
            WHERE sales = (
                SELECT MAX(sales)
                FROM superstore_raw s2
                WHERE s2.customer_id = s1.customer_id
            )
            ORDER BY sales DESC;
        """,

        "03_total_sales_per_customer.csv": """
            WITH customer_sales AS (
                SELECT
                    customer_id,
                    customer_name,
                    SUM(sales) AS total_sales
                FROM superstore_raw
                GROUP BY customer_id, customer_name
            )
            SELECT *
            FROM customer_sales
            ORDER BY total_sales DESC;
        """,

        "04_above_average_customer_sales.csv": """
            WITH customer_sales AS (
                SELECT
                    customer_id,
                    customer_name,
                    SUM(sales) AS total_sales
                FROM superstore_raw
                GROUP BY customer_id, customer_name
            )
            SELECT *
            FROM customer_sales
            WHERE total_sales > (
                SELECT AVG(total_sales)
                FROM customer_sales
            )
            ORDER BY total_sales DESC;
        """,

        "05_customer_sales_rank.csv": """
            WITH customer_sales AS (
                SELECT
                    customer_id,
                    customer_name,
                    SUM(sales) AS total_sales
                FROM superstore_raw
                GROUP BY customer_id, customer_name
            )
            SELECT
                customer_id,
                customer_name,
                total_sales,
                RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
            FROM customer_sales;
        """,

        "06_order_row_number_per_customer.csv": """
            SELECT
                customer_id,
                customer_name,
                order_id,
                order_date,
                sales,
                ROW_NUMBER() OVER (
                    PARTITION BY customer_id
                    ORDER BY sales DESC
                ) AS order_row_number
            FROM superstore_raw
            ORDER BY customer_id, order_row_number;
        """,

        "07_top_3_customers.csv": """
            WITH customer_sales AS (
                SELECT
                    customer_id,
                    customer_name,
                    SUM(sales) AS total_sales
                FROM superstore_raw
                GROUP BY customer_id, customer_name
            ),
            ranked_customers AS (
                SELECT
                    customer_id,
                    customer_name,
                    total_sales,
                    RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
                FROM customer_sales
            )
            SELECT *
            FROM ranked_customers
            WHERE sales_rank <= 3;
        """,

        "08_final_combined_query.csv": """
            WITH customer_sales AS (
                SELECT
                    customer_id,
                    SUM(sales) AS total_sales
                FROM orders
                GROUP BY customer_id
            ),
            ranked_customers AS (
                SELECT
                    customer_id,
                    total_sales,
                    RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
                FROM customer_sales
            )
            SELECT
                c.customer_name,
                rc.total_sales,
                rc.sales_rank
            FROM ranked_customers rc
            JOIN customers c
                ON rc.customer_id = c.customer_id
            ORDER BY rc.sales_rank;
        """,

        "09_top_5_customers.csv": """
            WITH customer_sales AS (
                SELECT
                    customer_id,
                    customer_name,
                    SUM(sales) AS total_sales
                FROM superstore_raw
                GROUP BY customer_id, customer_name
            )
            SELECT *
            FROM customer_sales
            ORDER BY total_sales DESC
            LIMIT 5;
        """,

        "10_bottom_5_customers.csv": """
            WITH customer_sales AS (
                SELECT
                    customer_id,
                    customer_name,
                    SUM(sales) AS total_sales
                FROM superstore_raw
                GROUP BY customer_id, customer_name
            )
            SELECT *
            FROM customer_sales
            ORDER BY total_sales ASC
            LIMIT 5;
        """,

        "11_single_order_customers.csv": """
            SELECT
                customer_id,
                customer_name,
                COUNT(DISTINCT order_id) AS order_count
            FROM superstore_raw
            GROUP BY customer_id, customer_name
            HAVING COUNT(DISTINCT order_id) = 1
            ORDER BY customer_name;
        """,

        "12_highest_order_value_per_customer.csv": """
            SELECT
                customer_id,
                customer_name,
                MAX(sales) AS highest_order_value
            FROM superstore_raw
            GROUP BY customer_id, customer_name
            ORDER BY highest_order_value DESC;
        """
    }

    # Run each query and save its output inside the results folder
    for file_name, query in queries_to_export.items():
        result_df = pd.read_sql_query(query, conn)
        result_df.to_csv(RESULTS_DIR / file_name, index=False)
        print(f"Saved: results/{file_name}")

    # Close database connection after all work is done
    conn.close()

    print("Assignment database and result files created successfully!")


# This makes sure the main function runs only when this file is executed directly
if __name__ == "__main__":
    main()