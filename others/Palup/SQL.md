## 設計一張資料表 並撰寫 sql 找出第一次登入後7天內還有登入的使用者 ##
例如：3/10第一次登入，3/12有再登入，滿足第一次登入後7天內還有登入

   - 任何 sql 語言回答皆可 
   - 簡單描述語法邏輯
   - 答案請提供 schema (column, type) 與 sql 



## Answer
- user_logins table schema
```sql
CREATE TABLE user_logins (
    user_id INT,
    login_time DATETIME,
    PRIMARY KEY (user_id, login_time)
);
```

- 找出第一次登入後7天內還有登入的使用者的SQL
  - 先做一個每個使用者的第一次登入時間的temporary table
    - 再根據第一次登入時間找出登入時間在第一次登入後7天內還有登入的使用者
```sql
WITH first_login AS (
    SELECT 
        user_id,
        MIN(login_time) AS first_login_time
    FROM user_logins
    GROUP BY user_id
)
SELECT 
    DISTINCT u.user_id
FROM user_logins u
JOIN first_login f ON u.user_id = f.user_id
WHERE u.login_time > f.first_login_time
AND u.login_time <= DATE_ADD(f.first_login_time, INTERVAL 7 DAY);
```
