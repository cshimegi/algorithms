CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `email` varchar(32) UNIQUE NOT NULL,
  `name` varchar(16) NOT NULL,
  `created_at` timestamp NOT NULL,
  `company_id` int NOT NULL
);

CREATE TABLE `user_roles` (
  `user_id` int NOT NULL,
  `role_id` int NOT NULL
);

CREATE TABLE `companies` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL
);

CREATE TABLE `roles` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(16) NOT NULL
);

CREATE TABLE `dashboards` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(128) NOT NULL,
  `config` text,
  `last_access_time` timestamp
);

ALTER TABLE `users` ADD FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`);

ALTER TABLE `user_roles` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `user_roles` ADD FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);

ALTER TABLE `dashboards` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
