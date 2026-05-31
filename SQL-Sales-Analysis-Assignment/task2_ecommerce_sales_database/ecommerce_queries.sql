-- Celebal Week 2 Task: E-Commerce Sales Database
-- Query Solutions

-- SECTION A: SQL Basics

-- Q1. Display all columns and rows from customers table.
SELECT *
FROM customers;

-- Q2. Retrieve first_name, last_name, and city of all customers.
SELECT first_name, last_name, city
FROM customers;

-- Q3. List all unique categories available in products table.
SELECT DISTINCT category
FROM products;

-- Q4. Primary Key explanation.
-- customers: customer_id
-- products: product_id
-- orders: order_id
-- order_items: item_id
-- A Primary Key must be unique and NOT NULL because it identifies each record separately.

-- Q5. Email constraints explanation.
-- The email column has UNIQUE and NOT NULL constraints.
-- If a duplicate email is inserted, the database rejects the insert operation.

-- Q6. Constraint violation test.
INSERT INTO products VALUES
(209, 'Test Product', 'Electronics', 'TestBrand', -50.00, 10);

-- This fails because CHECK (unit_price > 0) prevents negative product price.


-- SECTION B: Filtering and Optimization

-- Q7. Retrieve all delivered orders.
SELECT *
FROM orders
WHERE status = 'Delivered';

-- Q8. Find Electronics products with unit_price greater than 2000.
SELECT *
FROM products
WHERE category = 'Electronics'
  AND unit_price > 2000;

-- Q9. Customers who joined in 2024 and belong to Maharashtra.
SELECT *
FROM customers
WHERE join_date >= '2024-01-01'
  AND join_date < '2025-01-01'
  AND state = 'Maharashtra';

-- Q10. Orders between 2024-08-10 and 2024-08-25 that are not cancelled.
SELECT *
FROM orders
WHERE order_date BETWEEN '2024-08-10' AND '2024-08-25'
  AND status <> 'Cancelled';

-- Q11. Index explanation.
-- idx_orders_date is an index on order_date.
-- It helps the database search date-based records faster instead of scanning the complete table.

SELECT *
FROM orders
WHERE order_date BETWEEN '2024-08-01' AND '2024-08-20';

-- Q12. SARGable query explanation.
-- SELECT * FROM customers WHERE YEAR(join_date) = 2024;
-- This is not index-friendly because a function is applied on join_date.
-- Better query:

SELECT *
FROM customers
WHERE join_date >= '2024-01-01'
  AND join_date < '2025-01-01';


-- SECTION C: Aggregation

-- Q13. Count total number of orders.
SELECT COUNT(*) AS total_orders
FROM orders;

-- Q14. Total revenue from delivered orders.
SELECT SUM(total_amount) AS delivered_revenue
FROM orders
WHERE status = 'Delivered';

-- Q15. Average unit_price of products in each category.
SELECT category,
       ROUND(AVG(unit_price), 2) AS average_unit_price
FROM products
GROUP BY category;

-- Q16. Count of orders and total revenue by order status.
SELECT status,
       COUNT(*) AS order_count,
       SUM(total_amount) AS total_revenue
FROM orders
GROUP BY status
ORDER BY total_revenue DESC;

-- Q17. Most expensive and cheapest product in each category.
SELECT category,
       MAX(unit_price) AS most_expensive_product_price,
       MIN(unit_price) AS cheapest_product_price
FROM products
GROUP BY category;

-- Q18. Categories where average unit_price is greater than 2000.
SELECT category,
       ROUND(AVG(unit_price), 2) AS average_unit_price
FROM products
GROUP BY category
HAVING AVG(unit_price) > 2000;


-- SECTION D: Joins and Relationships

-- Q19. INNER JOIN orders with customers.
SELECT o.order_id,
       o.order_date,
       c.first_name,
       c.last_name,
       o.total_amount
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id;

-- Q20. LEFT JOIN all customers and their orders.
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       o.order_id,
       o.order_date,
       o.total_amount
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id;

-- Q21. JOIN orders, order_items, and products.
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

-- Q22. JOIN explanation.
-- LEFT JOIN returns all rows from the left table and matching rows from the right table.
-- Example: customers LEFT JOIN orders shows all customers even if they have no orders.
-- RIGHT JOIN returns all rows from the right table and matching rows from the left table.
-- FULL OUTER JOIN is used when we want all matched and unmatched records from both tables.

-- Q23. Foreign Key explanation.
-- orders.customer_id references customers.customer_id.
-- order_items.order_id references orders.order_id.
-- order_items.product_id references products.product_id.
-- If customer_id = 999 does not exist, inserting an order with customer_id = 999 fails.


-- SECTION E: Advanced Concepts

-- Q24. Classify products into price tiers.
SELECT product_name,
       unit_price,
       CASE
           WHEN unit_price < 1000 THEN 'Budget'
           WHEN unit_price BETWEEN 1000 AND 3000 THEN 'Mid-Range'
           WHEN unit_price > 3000 THEN 'Premium'
       END AS price_tier
FROM products;

-- Q25. Count delivered vs not delivered orders.
SELECT
    SUM(CASE WHEN status = 'Delivered' THEN 1 ELSE 0 END) AS delivered_orders,
    SUM(CASE WHEN status <> 'Delivered' THEN 1 ELSE 0 END) AS not_delivered_orders
FROM orders;

-- Q26. ACID explanation.
-- Atomicity: All steps of a transaction happen fully or none happen.
-- Consistency: Database moves from one valid state to another valid state.
-- Isolation: One transaction does not disturb another transaction.
-- Durability: Once data is committed, it remains saved even after system failure.
-- Example: In a bank transfer, money should be deducted from one account and added to another.
-- If one step fails, the complete transaction should rollback.

-- Q27. Transaction example.

BEGIN TRANSACTION;

INSERT INTO orders VALUES
(1011, 102, DATE('now'), 'Pending', 1598.00);

INSERT INTO order_items VALUES
(5016, 1011, 202, 1, 799.00, 0);

INSERT INTO order_items VALUES
(5017, 1011, 208, 1, 599.00, 0);

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 202;

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 208;

COMMIT;