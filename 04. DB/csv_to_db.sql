- 모든 테이블 삭제

DROP TABLE items;
DROP TABLE items2;
DROP TABLE orderitems;
DROP TABLE orderitems2;
DROP TABLE orders;
DROP TABLE orders2;
DROP TABLE stores;
DROP TABLE stores2;
DROP TABLE users;
DROP TABLE users2;


-csv 파일 db로 저장

.mode csv

.import ./csv/items.csv items

.import ./csv/orderitems.csv orderitems

.import ./csv/orders.csv orders

.import ./csv/stores.csv stores

.import ./csv/users.csv users


- id를 가진 table2 생성

CREATE TABLE IF NOT EXISTS users2(
"UUID" INTEGER PRIMARY KEY AUTOINCREMENT,
"Id" TEXT,
"Name" TEXT,
"Gender" TEXT,
"Age" INTEGER,
"Birthdate" DATETIME,
"Address" TEXT);

CREATE TABLE IF NOT EXISTS stores2(
"UUID" INTEGER PRIMARY KEY AUTOINCREMENT,
"Id" TEXT,
"Name" TEXT,
"Type" TEXT,
"Address" TEXT);

CREATE TABLE IF NOT EXISTS orders2(
"UUID" INTEGER PRIMARY KEY AUTOINCREMENT,
"Id" TEXT,
"OrderAt" DATETIME,
"StoreId" TEXT,
"UserId" TEXT);

CREATE TABLE IF NOT EXISTS items2(
"UUID" INTEGER PRIMARY KEY AUTOINCREMENT,
"Id" TEXT,
"Name" TEXT,
"Type" TEXT,
"UnitPrice" INTEGER);

CREATE TABLE IF NOT EXISTS orderitems2(
"UUID" INTEGER PRIMARY KEY AUTOINCREMENT,
"Id" TEXT,
"OrderId" TEXT,
"ItemId" TEXT);


- db로 저장한 csv 데이터 id 있는 테이블에 복제

INSERT INTO items2(Id,Name,Type,UnitPrice) 
SELECT Id,Name,Type,UnitPrice FROM items;

INSERT INTO orderitems2(Id,OrderId,ItemId) 
SELECT Id,OrderId,ItemId FROM orderitems;

INSERT INTO orders2(Id,OrderAt,StoreId,UserId) 
SELECT Id,OrderAt,StoreId,UserId FROM orders;

INSERT INTO stores2(Id,Name,Type,Address) 
SELECT Id,Name,Type,Address FROM stores;

INSERT INTO users2(Id,Name,Gender,Age,Birthdate,Address) 
SELECT Id,Name,Gender,Age,Birthdate,Address FROM users;


- csv로 만든 기존 테이블 삭제

DROP TABLE items;
DROP TABLE orderitems;
DROP TABLE orders;
DROP TABLE stores;
DROP TABLE users;


- 이름 바꾸기

ALTER TABLE items2 RENAME TO items;
ALTER TABLE orderitems2 RENAME TO orderitems;
ALTER TABLE orders2 RENAME TO orders;
ALTER TABLE stores2 RENAME TO stores;
ALTER TABLE users2 RENAME TO users;

-- ---------------------------------------------------------------------
SELECT users.Name,  users.Id, orders.Id, orders.OrderAt, orders.StoreId
FROM users
JOIN orders
ON users.Id = orders.UserId
WHERE users.Id='0a497257-2b1a-4836-940f-7b95db952e61';
