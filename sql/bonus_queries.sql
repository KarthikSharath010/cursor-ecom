-- 1. Top 5 customers by total spend
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    SUM(o.total_amount) AS total_spend
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spend DESC
LIMIT 5;

-- 2. Most popular products by quantity sold
SELECT
    p.product_id,
    p.name,
    SUM(oi.quantity) AS total_units_sold
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_units_sold DESC;

-- 3. Revenue per day for the last 30 days
SELECT
    o.order_date,
    SUM(o.total_amount) AS daily_revenue
FROM orders o
WHERE o.order_date >= date('now', '-30 days')
GROUP BY o.order_date
ORDER BY o.order_date DESC;

