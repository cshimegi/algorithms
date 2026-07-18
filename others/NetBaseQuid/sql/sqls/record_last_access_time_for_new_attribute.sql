UPDATE dashboards
SET
    last_access_time = NOW(),
    -- attribute_name and attribute_value depend on real use case. Here are examples only
    config = JSON_SET(config, '$.<attribute_name>', '<attribute_value>')
WHERE id = <dashboard_id>;