-- 1. Total revenue per customer
SELECT c.customer_id, c.customer_name,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS total_revenue
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY c.customer_id, c.customer_name
ORDER BY total_revenue DESC;

-- 2. Revenue per category
SELECT p.category,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS category_revenue
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
JOIN orders o ON o.order_id = oi.order_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY p.category
ORDER BY category_revenue DESC;

-- 3. Monthly revenue
SELECT strftime('%Y-%m', o.order_date) AS revenue_month,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS monthly_revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY revenue_month
ORDER BY revenue_month;

-- 4. Top products by quantity and revenue
SELECT p.product_id, p.product_name, p.category,
       SUM(oi.quantity) AS quantity_sold,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
JOIN orders o ON o.order_id = oi.order_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC;

-- 5. Average order value by customer segment
WITH order_values AS (
    SELECT o.order_id, c.customer_segment,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS order_value
    FROM orders o
    JOIN customers c ON c.customer_id = o.customer_id
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.order_status NOT IN ('Cancelled', 'Returned')
    GROUP BY o.order_id, c.customer_segment
)
SELECT customer_segment,
       ROUND(AVG(order_value), 2) AS average_order_value,
       COUNT(*) AS order_count
FROM order_values
GROUP BY customer_segment
ORDER BY average_order_value DESC;
