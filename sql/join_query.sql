SELECT
    c.first_name || ' ' || c.last_name AS customer_name,
    o.order_id,
    o.order_date,
    SUM(oi.quantity) AS item_count,
    SUM(oi.line_total) AS order_value,
    p.payment_method
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN payments p ON p.order_id = o.order_id
JOIN products pr ON pr.product_id = oi.product_id
GROUP BY
    c.customer_id,
    o.order_id,
    p.payment_method
ORDER BY
    order_value DESC;

