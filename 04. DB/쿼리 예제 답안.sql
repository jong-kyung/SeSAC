-- 1. non_usa_customers.sql: 미국에 거주하지 않는 고객(전체 이름, 고객 ID 및 국가)을 표시하는 쿼리를 제공합니다.
SELECT FirstName ||" "|| LastName AS 'Full Name', customerId, Country FROM customers WHERE country != 'USA';

-- 2. brazil_customers.sql: 브라질 고객만 표시하는 쿼리를 제공합니다.
SELECT FirstName ||" "|| LastName AS 'Full Name' 
FROM customers WHERE country == 'Brazil';

-- 3. brazil_customers_invoices.sql: 브라질 고객의 송장을 보여주는 쿼리를 제공합니다. 결과 테이블에는 고객의 전체 이름, 송장 ID, 송장 날짜 및 청구 국가가 표시되어야 합니다.
SELECT customers.FirstName ||" "|| customers.LastName AS 'Full Name',Invoices.InvoiceId, Invoices.InvoiceDate, Invoices.BillingCountry 
FROM Invoices INNER 
JOIN customers ON customers.Country == 'Brazil';

-- 강사님 풀이
SELECT c.FirstName ||" "|| c.LastName AS 'Full Name',I.InvoiceId, I.InvoiceDate, I.BillingCountry 
FROM Invoices I 
LEFT JOIN customers c ON i.CustomerId == c.CustomerId WHERE c.Country == 'Brazil';


-- 4. sales_agents.sql: 판매 대리인인 직원만 표시하는 쿼리를 제공하십시오.
SELECT FirstName ||" "|| LastName AS 'Full Name' 
FROM employees WHERE Title = 'Sales Support Agent';

-- 강사님 풀이
SELECT * FROM employees where title like 'Sales%';

-- 5. unique_invoice_countries.sql: 송장 테이블에서 청구 국가의 고유/고유 목록을 표시하는 쿼리를 제공합니다.
SELECT BillingCountry 
FROM Invoices 
Group By BillingCountry;

-- 강사님 풀이
SELECT DISTINCT BillingCountry FROM invoices;

-- 6. sales_agent_invoices.sql: 각 판매 에이전트와 연결된 송장을 표시하는 쿼리를 제공합니다. 결과 테이블에는 영업 에이전트의 전체 이름이 포함되어야 합니다.
SELECT Invoices.*, employees.FirstName ||" "|| employees.LastName AS 'Full Name' 
FROM employees 
INNER JOIN customers ON employees.employeeId == customers.SupportRepId 
INNER JOIN Invoices ON customers.customerId == invoices.invoiceId;

-- 7. invoice_totals.sql: 모든 송장 및 고객에 대한 송장 합계, 고객 이름, 국가 및 판매 대리점 이름을 표시하는 쿼리를 제공합니다.
SELECT invoices.*, customers.FirstName ||" "|| customers.LastName AS 'Full Name', customers.Country, employees.FirstName ||" "|| employees.LastName AS 'employee Full Name' 
FROM invoices 
INNER JOIN customers ON invoices.CustomerId == customers.CustomerId INNER JOIN employees ON customers.SupportRepId == employees.employeeId;

-- 8. total_invoices_{year}.sql: 2009년과 2011년에 몇 개의 인보이스가 있었습니까?
SELECT count(*) 
FROM invoices 
WHERE InvoiceDate BETWEEN '2009-01-01' AND '2011-12-31';

-- 강사님 풀이1
SELECT count(*) 
FROM invoices 
WHERE InvoiceDate 
BETWEEN '2009-01-01' AND '2009-12-31' 
OR InvoiceDate
BETWEEN '2011-01-01' AND '2011-12-31';

-- 강사님 풀이2
-- strftime
SELECT COUNT(i.InvoiceId) AS NumberOfInvoices, strftime('%Y', i.InvoiceId) AS InvoiceYear
FROM invoices I
WHERE InvoiceYear IN ('2009', '2011') 
GROUP BY InvoiceYear;

-- 9. total_sales_{year}.sql: 각 연도의 총 매출은 얼마입니까?
SELECT substr(invoices.InvoiceDate, 1, 4), sum(UnitPrice) 
FROM invoice_items 
INNER JOIN invoices ON invoice_items.InvoiceId == invoices.InvoiceId 
GROUP BY substr(invoices.InvoiceDate, 1, 4);

-- 10. invoice_37_line_item_count.sql: InvoiceLine 테이블을 보고 Invoice ID 37에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다.
SELECT count(*) 
FROM invoice_items 
WHERE InvoiceId == '37';

-- 11. line_items_per_invoice.sql: InvoiceLine 테이블을 보고 각 Invoice에 대한 라인 항목 수를 계산하는 쿼리를 제공합니다. 힌트: 그룹화 기준
SELECT invoice_items.InvoiceLineId, count(invoice_items.InvoiceId) 
FROM invoice_items 
INNER JOIN invoices ON invoice_items.InvoiceId == invoices.InvoiceId GROUP BY invoice_items.InvoiceId;

-- 강사님 풀이
SELECT invoiceId, COUNT(invoiceLineId) AS 'Invoice Count'
FROM invoice_items
GROUP BY invoiceID

-- 12. line_item_track.sql: 각 송장 라인 항목에 구매한 트랙 이름을 포함하는 쿼리를 제공합니다.
SELECT tracks.Name FROM tracks 
INNER JOIN invoice_items ON tracks.TrackId == invoice_items.TrackId;

-- 13. line_item_track_artist.sql: 구매한 트랙 이름과 아티스트 이름을 포함하는 쿼리를 각 송장 라인 항목과 함께 제공합니다.
SELECT tracks.Name, artists.Name FROM tracks 
INNER JOIN invoice_items ON tracks.trackId == invoice_items.trackId INNER JOIN albums ON tracks.AlbumId == albums.AlbumId
INNER JOIN artists ON albums.ArtistId == artists.ArtistId; 

-- 14. country_invoices.sql: 국가별 송장 수를 표시하는 쿼리를 제공합니다. 힌트: 그룹화 기준
SELECT customers.Country, count(customers.Country) 
FROM customers 
INNER JOIN invoices ON customers.customerId == invoices.customerId GROUP BY customers.Country;

-- 15. playlists_track_count.sql: 각 재생 목록의 총 트랙 수를 표시하는 쿼리를 제공합니다. 재생 목록 이름은 결과 테이블에 포함되어야 합니다.
SELECT playlists.Name, count(playlist_track.TrackId) 
FROM playlist_track 
INNER JOIN playlists ON playlist_track.PlaylistId == playlists.PlaylistId 
INNER JOIN tracks ON playlist_track.TrackId == Tracks.TrackId 
GROUP BY playlists.Name;

-- 16. Tracks_no_id.sql: 모든 트랙을 표시하지만 ID는 표시하지 않는 쿼리를 제공합니다. 결과에는 앨범 이름, 미디어 유형 및 장르가 포함되어야 합니다.
SELECT tracks.Name, albums.Title, media_types.Name 
FROM tracks 
INNER JOIN albums ON tracks.AlbumId == albums.AlbumId 
INNER JOIN media_types ON tracks.MediaTypeId == media_types.MediaTypeId;

-- 17. invoices_line_item_count.sql: 모든 송장을 표시하지만 송장 라인 항목의 수를 포함하는 쿼리를 제공합니다.
SELECT invoices.*, count(invoice_items.InvoiceLineId) 
FROM invoices 
INNER JOIN invoice_items ON invoices.invoiceId == invoice_items.invoiceId 
GROUP BY invoices.invoiceId;

-- 18. sales_agent_total_sales.sql: 판매 대리점별 총 매출을 조회하는 쿼리를 제공한다.
SELECT employees.FirstName ||" "|| employees.LastName AS 'Full Name', SUM(invoice_items.UnitPrice) 
FROM invoices
INNER JOIN invoice_items ON invoices.InvoiceId == invoice_items.InvoiceId 
INNER JOIN customers ON invoices.CustomerId == customers.CustomerId 
INNER JOIN employees ON customers.SupportRepId == employees.EmployeeId 
GROUP BY employees.FirstName;

-- 19. top_2009_agent.sql: 2009년 가장 많은 매출을 올린 판매원은?
SELECT substr(invoices.InvoiceDate, 1, 4), employees.FirstName, SUM(invoice_items.UnitPrice) 
FROM invoices 
INNER JOIN customers ON invoices.CustomerId == customers.CustomerId 
INNER JOIN employees ON customers.SupportRepId == employees.employeeId 
INNER JOIN invoice_items ON invoices.InvoiceId == invoice_items.InvoiceId 
WHERE substr(invoices.InvoiceDate, 1, 4) == '2009' 
ORDER BY SUM(invoice_items.UnitPrice);

-- 20. sales_agent_customer_count.sql: 각 판매 대리점에 할당된 고객 수를 보여주는 쿼리를 제공한다.
SELECT employees.FirstName, count(customers.FirstName) 
FROM customers 
INNER JOIN employees ON customers.SupportRepId == employees.employeeId 
GROUP BY employees.FirstName;

-- 21. sales_agent_customer_count.sql: 각 판매 대리점에 할당된 고객 수를 보여주는 쿼리를 제공한다.
SELECT employees.FirstName ,count(customers.FirstName) 
FROM employees 
INNER JOIN customers ON employees.employeeId == customers.SupportRepId 
GROUP BY employees.FirstName;

-- 22. sales_per_country.sql: 국가별 총 매출을 보여주는 쿼리를 제공한다.
SELECT customers.Country, SUM(invoice_items.UnitPrice) 
FROM invoices 
INNER JOIN invoice_items ON invoices.InvoiceId == invoice_items.InvoiceId
INNER JOIN customers ON invoices.CustomerId == customers.CustomerId 
GROUP BY customers.Country;

-- 23. top_country.sql: 고객이 가장 많이 지출한 국가는 어디입니까?
SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice) 
FROM invoices 
INNER JOIN invoice_items ON invoices.InvoiceId == invoice_items.InvoiceId 
INNER JOIN customers ON invoices.CustomerId == customers.CustomerId 
GROUP BY invoices.BillingCountry 
ORDER BY SUM(invoice_items.UnitPrice) 
DESC LIMIT 1;

-- 강사님 풀이
-- Nested Query : SELECT FROM 안에 SELECT가 쓰이는 것, 효율적이지는 않기에 고민을 많이 해보아야함.
SELECT "Country", MAX("Total Sales For Country") as "Total Spent"
FROM (
    SELECT BillingCountry as "Country", SUM(Total) as "Total Sales For Country"
    FROM invoices
    GROUP BY BillingCountry
);


-- 24. top_2013_track.sql: 2013년 가장 많이 구매한 트랙을 보여주는 쿼리를 제공합니다.
SELECT tracks.Name, SUM(invoice_items.trackId) 
FROM invoice_items
INNER JOIN tracks ON tracks.TrackId == invoice_items.TrackId
INNER JOIN invoices ON invoice_items.InvoiceID == invoices.InvoiceId 
INNER JOIN customers ON invoices.CustomerId == customers.CustomerId 
WHERE substr(invoices.InvoiceDate, 1, 4) == '2013' 
GROUP BY tracks.Name 
ORDER BY SUM(invoice_items.trackId) 
DESC LIMIT 1;

-- 25. top_5_tracks.sql: 가장 많이 구매한 상위 5곡을 보여주는 쿼리를 제공합니다.
SELECT tracks.Name, SUM(invoice_items.trackId) 
FROM invoice_items
INNER JOIN tracks ON tracks.TrackId == invoice_items.TrackId
INNER JOIN invoices ON invoice_items.InvoiceID == invoices.InvoiceId 
INNER JOIN customers ON invoices.CustomerId == customers.CustomerId 
GROUP BY tracks.Name 
ORDER BY SUM(invoice_items.trackId) 
DESC LIMIT 5;

-- 강사님 풀이
SELECT t.Name, COUNT(t.Name) AS 'PurchaseCount'
FROM tracks t
JOIN invoice_items I ON I.TrackId = t.TrackId
GROUP BY t.Name
ORDER BY PurchaseCount
DESC LIMIT 5;

-- 26. top_3_artists.sql: 가장 많이 팔린 3명의 아티스트를 보여주는 쿼리를 제공합니다.
SELECT artists.Name, count(invoice_items.trackId) 
FROM invoice_items
INNER JOIN tracks ON invoice_items.TrackId == tracks.TrackId
INNER JOIN albums ON tracks.AlbumId == albums.AlbumId
INNER JOIN artists ON albums.ArtistId == artists.ArtistId
INNER JOIN invoices ON invoice_items.InvoiceId == invoices.InvoiceId 
GROUP BY artists.Name 
ORDER BY count(invoice_items.trackId) 
DESC LIMIT 3;

-- 27. top_media_type.sql: 가장 많이 구매한 Media Type을 보여주는 쿼리를 제공한다.
SELECT media_types.Name, count(invoice_items.InvoiceId) 
FROM media_types 
INNER JOIN tracks ON media_types.MediaTypeId == tracks.MediaTypeId 
INNER JOIN invoice_items ON invoice_items.TrackId == tracks.TrackId 
INNER JOIN invoices ON invoice_items.InvoiceId == invoices.InvoiceId 
GROUP BY media_types.Name 
ORDER BY count(invoice_items.InvoiceId) 
DESC LIMIT 1;