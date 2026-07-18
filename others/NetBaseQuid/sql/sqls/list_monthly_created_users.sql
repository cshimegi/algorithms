SELECT
    DATE_FORMAT(created_at, '%Y-%m') AS created_month,
    COUNT(*) AS user_count
FROM users
GROUP BY created_month
ORDER BY created_month;