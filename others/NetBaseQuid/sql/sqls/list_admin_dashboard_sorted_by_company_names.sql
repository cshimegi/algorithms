SELECT
    c.name AS company_name,
    COUNT(d.id) AS dashboard_count
FROM dashboards d
    JOIN users u ON d.user_id = u.id
    JOIN companies c ON u.company_id = c.id
    JOIN user_roles ur ON u.id = ur.user_id
    JOIN roles r ON ur.role_id = r.id
WHERE r.name = 'admin'
GROUP BY c.name
ORDER BY c.name;