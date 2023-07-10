-- 1. 사용자별로 몇번의 주문을 했는지 많이 주문한 순서로 보여주기
SELECT orders.userId, count(orders.userId) AS 'OrderCount' 
FROM orders
GROUP BY orders.userId
ORDER BY OrderCount DESC;

-- 2. store의 주소와 user의 주소가 같은동네인지 보여주기
SELECT users.Name, stores.Name, substr(users.Address, 1, 2)
FROM users
INNER JOIN stores ON substr(users.Address, 1, 2) = substr(stores.Address, 1, 2);

-- 3. 주문한 사람과 주문한 상품이 뭔지 보여주기
SELECT users.Name, items.Name
FROM users
INNER JOIN orders ON users.Id = orders.userId
INNER JOIN orderitems ON orders.Id = orderitems.OrderId
INNER JOIN items ON orderitems.ItemId = items.Id
GROUP BY users.Name;

-- 4. 주문한 사람과 주문한 상품과 가격이 얼마인지 보여주기
SELECT users.Name, items.Name, items.UnitPrice
FROM users
INNER JOIN orders ON users.Id = orders.userId
INNER JOIN orderitems ON orders.Id = orderitems.OrderId
INNER JOIN items ON orderitems.ItemId = items.Id
GROUP BY users.Name;

-- 5. 각 지역별로 매장이 몇개 있는지 찾기
SELECT substr(stores.Address, 1, 2) AS 'City', count(stores.Name) AS 'StoresCount'
FROM stores
GROUP BY City

-- 6. 2023년 5월의 방문객이 가장 많은 지점 찾기
SELECT stores.Name, count(stores.Name) AS 'TopRate'
FROM stores
INNER JOIN orders ON stores.Id = orders.StoreId
WHERE substr(orders.OrderAt, 1, 4) == '2023'
AND substr(orders.OrderAt, 6, 2) == '05'
GROUP BY stores.Name
ORDER BY TopRate
DESC LIMIT 1;

-- 7. 주문을 가장 많이한 사용자 찾기
SELECT users.Name, count(orders.UserId) AS 'TopRate'
FROM users 
INNER JOIN orders ON users.Id = orders.UserId
GROUP BY users.Name
ORDER BY TopRate
DESC LIMIT 1;

-- 8. 각 사용자가 사용한 금액 보여주기
SELECT users.Name, SUM(items.UnitPrice) AS 'price'
FROM users
INNER JOIN orders ON users.Id = orders.UserId
INNER JOIN orderitems ON orders.Id = orderitems.OrderId
INNER JOIN items ON orderitems.ItemId = items.Id
GROUP BY users.Name
ORDER BY Price DESC;

-- 9. 어떤 종류의 음료가 가장 많이 팔렸는지 확인하기
SELECT items.Type, count(orderitems.itemId) AS 'purchasedCount'
FROM items
INNER JOIN orderitems ON items.Id = orderitems.ItemId
GROUP BY items.Type
ORDER BY purchasedCount DESC;

-- 10. 각 성별별로 어떤 상품을 가장 많이 샀는지 확인하기
SELECT users.Gender, items.Name ,count(orderitems.ItemId) AS 'purchaseCount'
FROM users 
INNER JOIN orders ON users.Id = orders.UserId
INNER JOIN orderitems On orders.Id = orderitems.OrderId
INNER JOIN items ON orderitems.ItemId = items.Id
GROUP BY users.Gender;

-- --------------------------------------------------------
-- 강사님) 특정 사용자가 구매한 주문 내역을 모두 보여주시오.
SELECT users.Name, orders.*
FROM users
LEFT JOIN orders ON users.Id = orders.UserId
INNER JOIN orderitems ON orders.Id = orderitems.OrderId
WHERE users.Name = '최서준'

-- 강사님) 특정 사용자가 구매한 주문 내역의 상품명을 모두 보여주시오.
SELECT users.Name, items.Name
FROM users
LEFT JOIN orders ON users.Id = orders.UserId
INNER JOIN orderitems ON orders.Id = orderitems.OrderId
INNER JOIN items ON orderitems.ItemId = items.Id
WHERE users.Name = '최서준'

-- 강사님) 특정 사용자가 구매한 매출액의 합산을 구하시오
SELECT users.Name, sum(items.UnitPrice) AS 'purchase'
FROM users
INNER JOIN orders ON users.Id = orders.UserId
INNER JOIN orderitems ON orders.Id = orderitems.OrderId
INNER JOIN items ON orderitems.ItemId = items.Id
WHERE users.Name = '최서준'

-- 강사님) 상점별 월간 통계(매출액)을 구하시오
SELECT stores.Name, substr(orders.OrderAt, 6, 2) AS 'Month', AVG(items.UnitPrice) AS 'Total'
FROM stores
INNER JOIN orders ON stores.Id = orders.StoreId
INNER JOIN orderitems ON orders.Id = orderitems.OrderId
INNER JOIN items ON orderitems.ItemId = items.Id
GROUP BY stores.Name
ORDER BY Month