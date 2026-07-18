-- Insert companies
INSERT INTO companies (name) VALUES ('QUID'), ('Rakuten');

-- Insert roles (Make sure you have an 'admin' role)
INSERT INTO roles (name) VALUES ('admin'), ('analyst'), ('viewer');

-- Insert users (Make sure company_id corresponds to the companies you just inserted)
INSERT INTO users (email, name, created_at, company_id)
VALUES
    ('abc@example.com', 'James', '2025-02-16 10:00:00', 1),  -- Assuming company_id 1 is Acme Corp
    ('abc2@example.com', 'Jerry', '2025-02-17 11:00:00', 1),
    ('abc3@example.com', 'Alan', '2025-02-18 09:00:00', 2); -- Assuming company_id 2 is Globex Inc.

-- Link users to roles
INSERT INTO user_roles (user_id, role_id) VALUES (1, 1); -- Assuming role_id 1 is 'admin'
INSERT INTO user_roles (user_id, role_id) VALUES (2, 2); -- Assuming role_id 2 is 'analyst'
INSERT INTO user_roles (user_id, role_id) VALUES (3, 3); -- Assuming role_id 3 is 'viewer'

-- Insert dashboards (Make sure user_id corresponds to the users you just inserted)
INSERT INTO dashboards (user_id, name, config)
VALUES
    (1, 'Coding Tests', '{ "type": "bar", "data": { ... } }'),
    (1, 'Marketing Analysis', '{ "type": "line", "data": { ... } }'),
    (2, 'API Traffic', '{ "type": "pie", "data": { ... } }'),
    (2, 'User Segmentation', '{ "type": "scatter", "data": { ... } }'),
    (3, 'API Performance', '{ "type": "table", "data": { ... } }');