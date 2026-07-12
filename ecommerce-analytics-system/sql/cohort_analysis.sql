-- Cohort retention analysis based on first purchase month
WITH customer_orders AS (
    SELECT DISTINCT customer_id, strftime('%Y-%m', order_date) AS activity_month
    FROM orders
    WHERE order_status NOT IN ('Cancelled', 'Returned')
), first_purchase AS (
    SELECT customer_id, MIN(activity_month) AS cohort_month
    FROM customer_orders
    GROUP BY customer_id
), cohort_activity AS (
    SELECT co.customer_id, fp.cohort_month, co.activity_month,
           ((CAST(substr(co.activity_month, 1, 4) AS INTEGER) - CAST(substr(fp.cohort_month, 1, 4) AS INTEGER)) * 12
            + CAST(substr(co.activity_month, 6, 2) AS INTEGER) - CAST(substr(fp.cohort_month, 6, 2) AS INTEGER)) AS month_number
    FROM customer_orders co
    JOIN first_purchase fp ON fp.customer_id = co.customer_id
), cohort_sizes AS (
    SELECT cohort_month, COUNT(DISTINCT customer_id) AS cohort_size
    FROM first_purchase
    GROUP BY cohort_month
), retention AS (
    SELECT cohort_month, month_number, COUNT(DISTINCT customer_id) AS retained_customers
    FROM cohort_activity
    GROUP BY cohort_month, month_number
)
SELECT r.cohort_month, r.month_number, cs.cohort_size, r.retained_customers,
       ROUND(r.retained_customers * 100.0 / cs.cohort_size, 2) AS retention_rate_percent
FROM retention r
JOIN cohort_sizes cs ON cs.cohort_month = r.cohort_month
ORDER BY r.cohort_month, r.month_number;

-- Repeat and churn status using 180 days without purchase as a practical churn rule
WITH customer_stats AS (
    SELECT c.customer_id, c.customer_name,
           COUNT(DISTINCT o.order_id) AS order_count,
           MAX(o.order_date) AS last_order_date
    FROM customers c
    LEFT JOIN orders o ON o.customer_id = c.customer_id
                       AND o.order_status NOT IN ('Cancelled', 'Returned')
    GROUP BY c.customer_id, c.customer_name
)
SELECT customer_id, customer_name, order_count, last_order_date,
       CASE
         WHEN order_count = 0 THEN 'No purchase'
         WHEN order_count = 1 THEN 'One-time customer'
         WHEN julianday('now') - julianday(last_order_date) > 180 THEN 'Churned customer'
         ELSE 'Repeat customer'
       END AS customer_status
FROM customer_stats
ORDER BY order_count DESC;
