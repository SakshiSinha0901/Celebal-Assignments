all_queries = {
    "01_schema": "PRAGMA table_info(sales_data);",
    "02_sample_data": "SELECT * FROM sales_data LIMIT 10;",
    "03_total_rows": "SELECT COUNT(*) AS total_rows FROM sales_data;",
    "04_filter_region_west": "SELECT order_id, customer_name, region, sales, profit FROM sales_data WHERE region = 'West' LIMIT 10;",
    "05_filter_category_technology": "SELECT order_id, category, sub_category, sales, profit FROM sales_data WHERE category = 'Technology' LIMIT 10;",
    "06_filter_date": "SELECT order_id, order_date, sales, profit FROM sales_data WHERE order_date >= '2017-01-01' LIMIT 10;",
    "07_filter_sales_above_500": "SELECT order_id, customer_name, category, sales, profit FROM sales_data WHERE sales > 500 ORDER BY sales DESC LIMIT 10;",
    "08_multiple_filters": "SELECT order_id, region, category, sales, profit FROM sales_data WHERE region = 'East' AND category = 'Furniture' AND sales > 300 ORDER BY sales DESC LIMIT 10;",
    "09_sales_by_region": "SELECT region, ROUND(SUM(sales), 2) AS total_sales FROM sales_data GROUP BY region ORDER BY total_sales DESC;",
    "10_profit_by_region": "SELECT region, ROUND(SUM(profit), 2) AS total_profit FROM sales_data GROUP BY region ORDER BY total_profit DESC;",
    "11_sales_quantity_by_category": "SELECT category, ROUND(SUM(sales), 2) AS total_sales, SUM(quantity) AS total_quantity FROM sales_data GROUP BY category ORDER BY total_sales DESC;",
    "12_average_sales_by_category": "SELECT category, ROUND(AVG(sales), 2) AS average_sales FROM sales_data GROUP BY category ORDER BY average_sales DESC;",
    "13_profit_by_sub_category": "SELECT sub_category, ROUND(SUM(profit), 2) AS total_profit FROM sales_data GROUP BY sub_category ORDER BY total_profit DESC;",
    "14_top_10_products_by_sales": "SELECT product_name, ROUND(SUM(sales), 2) AS total_sales FROM sales_data GROUP BY product_name ORDER BY total_sales DESC LIMIT 10;",
    "15_top_10_products_by_profit": "SELECT product_name, ROUND(SUM(profit), 2) AS total_profit FROM sales_data GROUP BY product_name ORDER BY total_profit DESC LIMIT 10;",
    "16_top_categories_by_sales": "SELECT category, ROUND(SUM(sales), 2) AS total_sales FROM sales_data GROUP BY category ORDER BY total_sales DESC;",
    "17_top_states_by_sales": "SELECT state, ROUND(SUM(sales), 2) AS total_sales FROM sales_data GROUP BY state ORDER BY total_sales DESC LIMIT 10;",
    "18_monthly_sales_trend": "SELECT strftime('%Y-%m', order_date) AS month, ROUND(SUM(sales), 2) AS monthly_sales, ROUND(SUM(profit), 2) AS monthly_profit FROM sales_data GROUP BY month ORDER BY month;",
    "19_yearly_sales_trend": "SELECT strftime('%Y', order_date) AS year, ROUND(SUM(sales), 2) AS yearly_sales, ROUND(SUM(profit), 2) AS yearly_profit FROM sales_data GROUP BY year ORDER BY year;",
    "20_top_customers_by_sales": "SELECT customer_name, ROUND(SUM(sales), 2) AS total_sales FROM sales_data GROUP BY customer_name ORDER BY total_sales DESC LIMIT 10;",
    "21_top_customers_by_profit": "SELECT customer_name, ROUND(SUM(profit), 2) AS total_profit FROM sales_data GROUP BY customer_name ORDER BY total_profit DESC LIMIT 10;",
    "22_duplicate_order_ids": "SELECT order_id, COUNT(*) AS duplicate_count FROM sales_data GROUP BY order_id HAVING COUNT(*) > 1 ORDER BY duplicate_count DESC LIMIT 10;",
    "23_duplicate_row_ids": "SELECT row_id, COUNT(*) AS duplicate_count FROM sales_data GROUP BY row_id HAVING COUNT(*) > 1;",
    "24_loss_making_products": "SELECT product_name, ROUND(SUM(sales), 2) AS total_sales, ROUND(SUM(profit), 2) AS total_profit FROM sales_data GROUP BY product_name HAVING total_profit < 0 ORDER BY total_profit ASC LIMIT 10;",
    "25_missing_values_check": "SELECT SUM(CASE WHEN order_id IS NULL THEN 1 ELSE 0 END) AS missing_order_id, SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) AS missing_order_date, SUM(CASE WHEN customer_name IS NULL THEN 1 ELSE 0 END) AS missing_customer_name, SUM(CASE WHEN sales IS NULL THEN 1 ELSE 0 END) AS missing_sales, SUM(CASE WHEN profit IS NULL THEN 1 ELSE 0 END) AS missing_profit FROM sales_data;",
    "26_negative_sales_check": "SELECT * FROM sales_data WHERE sales < 0;",
    "27_negative_quantity_check": "SELECT * FROM sales_data WHERE quantity < 0;",
    "28_date_range_validation": "SELECT MIN(order_date) AS first_order_date, MAX(order_date) AS last_order_date FROM sales_data;"
}

with open(SQL_FILE, "w", encoding="utf-8") as f:
    f.write("-- Superstore Sales Analysis using SQL\n\n")
    for name, query in all_queries.items():
        f.write(f"-- {name}\n")
        f.write(query)
        f.write("\n\n")

print("sales_analysis.sql file created successfully.")