-- Customer lifetime value ranking
WITH customer_value AS (
    SELECT c.customer_id, c.customer_name,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS lifetime_value
    FROM customers c
    JOIN orders o ON o.customer_id = c.customer_id
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.order_status NOT IN ('Cancelled', 'Returned')
    GROUP BY c.customer_id, c.customer_name
)
SELECT customer_id, customer_name, ROUND(lifetime_value, 2) AS lifetime_value,
       RANK() OVER (ORDER BY lifetime_value DESC) AS value_rank,
       DENSE_RANK() OVER (ORDER BY lifetime_value DESC) AS dense_value_rank
FROM customer_value
ORDER BY value_rank;

-- Monthly revenue, running total and 3-month moving average
WITH monthly_revenue AS (
    SELECT strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.order_status NOT IN ('Cancelled', 'Returned')
    GROUP BY month
)
SELECT month,
       ROUND(revenue, 2) AS revenue,
       ROUND(SUM(revenue) OVER (ORDER BY month), 2) AS running_revenue,
       ROUND(AVG(revenue) OVER (
           ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ), 2) AS moving_average_3_month
FROM monthly_revenue
ORDER BY month;

-- Month-over-month growth rate using CTE and LAG
WITH monthly_revenue AS (
    SELECT strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.order_status NOT IN ('Cancelled', 'Returned')
    GROUP BY month
), revenue_with_previous AS (
    SELECT month, revenue,
           LAG(revenue) OVER (ORDER BY month) AS previous_revenue
    FROM monthly_revenue
)
SELECT month, ROUND(revenue, 2) AS revenue,
       ROUND(previous_revenue, 2) AS previous_revenue,
       CASE WHEN previous_revenue IS NULL OR previous_revenue = 0 THEN NULL
            ELSE ROUND((revenue - previous_revenue) * 100.0 / previous_revenue, 2)
       END AS growth_rate_percent
FROM revenue_with_previous
ORDER BY month;
