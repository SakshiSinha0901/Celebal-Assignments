-- Assignment 3: SQL Subqueries, CTEs and Window Functions
-- Dataset: Superstore Sales Data

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;

-- Step 1: Create customers table
CREATE TABLE customers AS
SELECT DISTINCT
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
FROM superstore_raw;

-- Step 2: Create orders table
CREATE TABLE orders AS
SELECT DISTINCT
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    product_id,
    sales,
    quantity,
    discount,
    profit
FROM superstore_raw;

-- Step 3: Create products table
CREATE TABLE products AS
SELECT DISTINCT
    product_id,
    category,
    sub_category,
    product_name
FROM superstore_raw;

-- Query 1: Find all orders where sales are greater than average sales
SELECT
    order_id,
    customer_id,
    customer_name,
    product_name,
    sales
FROM superstore_raw
WHERE sales > (
    SELECT AVG(sales)
    FROM superstore_raw
)
ORDER BY sales DESC;

-- Query 2: Find highest sales order for each customer
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

-- Query 3: Calculate total sales for each customer using CTE
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

-- Query 4: Find customers whose total sales are above average
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

-- Query 5: Rank all customers based on total sales
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

-- Query 6: Assign row numbers to each order within a customer
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

-- Query 7: Display top 3 customers based on total sales
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

-- Final Combined Query: JOIN + CTE + Window Function
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

-- Mini Project Query 1: Top 5 customers
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

-- Mini Project Query 2: Bottom 5 customers
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

-- Mini Project Query 3: Customers who made only one order
SELECT
    customer_id,
    customer_name,
    COUNT(DISTINCT order_id) AS order_count
FROM superstore_raw
GROUP BY customer_id, customer_name
HAVING COUNT(DISTINCT order_id) = 1
ORDER BY customer_name;

-- Mini Project Query 4: Customers with above-average total sales
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

-- Mini Project Query 5: Highest order value per customer
SELECT
    customer_id,
    customer_name,
    MAX(sales) AS highest_order_value
FROM superstore_raw
GROUP BY customer_id, customer_name
ORDER BY highest_order_value DESC;