-- Remove duplicates from customers table
DELETE c1
FROM customers c1
JOIN customers c2 ON c1.user_id = c2.user_id
                  AND c1.event_time = c2.event_time
                  AND c1.user_session = c2.user_session
                  AND c1.product_id = c2.product_id
                  AND c1.price = c2.price
                  AND c1.event_type = c2.event_type
                  AND c1.id > c2.id
WHERE ABS(TIMESTAMPDIFF(MINUTE, c1.event_time, c2.event_time)) <= 1;

