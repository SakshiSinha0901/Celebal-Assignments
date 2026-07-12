-- Frequency, spend tier and RFM-style customer segmentation
WITH customer_metrics AS (
    SELECT c.customer_id, c.customer_name,
           CAST(julianday('now') - julianday(MAX(o.order_date)) AS INTEGER) AS recency_days,
           COUNT(DISTINCT o.order_id) AS frequency,
           COALESCE(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 0) AS monetary
    FROM customers c
    LEFT JOIN orders o ON o.customer_id = c.customer_id
                       AND o.order_status NOT IN ('Cancelled', 'Returned')
    LEFT JOIN order_items oi ON oi.order_id = o.order_id
    GROUP BY c.customer_id, c.customer_name
), scored AS (
    SELECT *,
           NTILE(3) OVER (ORDER BY recency_days DESC) AS recency_score,
           NTILE(3) OVER (ORDER BY frequency) AS frequency_score,
           NTILE(3) OVER (ORDER BY monetary) AS monetary_score
    FROM customer_metrics
)
SELECT customer_id, customer_name, recency_days, frequency,
       ROUND(monetary, 2) AS monetary,
       CASE WHEN frequency <= 1 THEN 'One-time'
            WHEN frequency BETWEEN 2 AND 4 THEN 'Occasional'
            ELSE 'Loyal' END AS frequency_segment,
       CASE WHEN monetary < 10000 THEN 'Low'
            WHEN monetary < 50000 THEN 'Medium'
            ELSE 'High' END AS spend_tier,
       recency_score || frequency_score || monetary_score AS rfm_score
FROM scored
ORDER BY monetary DESC;
