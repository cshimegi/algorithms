# 給定一組資料舉例如下

|  post_id  |  user_id  |   lat    |    lon    | created_at |
------------|-----------|----------|-----------|------------|
| post_id_0 | user_id_3 |23.6468392|120.5358431|1616479608  |
| post_id_1 | user_id_1 |22.7344496|120.2845859|1616479408  |
| post_id_2 | user_id_3 |21.6468376|121.6538431|1616589608  |
| ...       | ...       |...       |...        |...         |


### NoSQL DB 優勢在於海量資料存取，速度快且成本低，雖然不像SQL DB可以下語法去拉出資料，但合理的rowkey設計可以做到預先準備好類SQL的statement效果，也能發揮NoSQL DB的最大效能

### (例如rowkey設計為post_id#user_id，則可以快速找出特定post_id的user_id是什麼)

## 問題A
設計一個NoSQL DB的rowkey，並說明設計原因，滿足
   - 找出某個user的post
   - 可由新到舊且由舊到新查找
   - 依照NoSQL DB特性，避免hotspot產生

## Answer A
我們可以設計rowkey為 user_id#created_at#post_id 這樣可以快速找到特定user的post並由新到舊且由舊到新查找。
如果要避免hotspot產生的話，可以設計rowkey為shard_id#user_id#created_at#post_id
shard_id = (hash(user_id) + timestamp / T) % N; T為time window大小, N為shard數量
藉此根據hash(user_id)以及時間的變化來創作不同的shard_id,避免hotspot。


## 問題B
設計一個NoSQL DB的rowkey，並說明設計原因，滿足
   - 在某個latlngbounds時，能快速找出結果
   - 依照NoSQL DB特性，避免hotspot產生


## Answer B
我們可以geo_hash 將某個範圍內的(lat, lon)轉成相同的hash value，
設計rowkey為 shard_id＃geo_hash#timestamp#post_id 這樣可以快速找出某個地理範圍內的結果。
shard_id = (geo_hash + timestamp / T) % N; T為time window大小, N為shard數量
藉此根據geo_hash以及時間的變化來創作不同的shard_id,避免hotspot。