'''

Graded Challenge 2

Nama	: Livia Amanda Annafiah
Batch	: BSD-005

Tujuan dari program ini adalah untuk mengelola data dari divisi Finance yang sebelummnya tersedia dalam format CSV. Proses ini mencakup *cleaning* dan normalisasi data, pembuatan database di PostgreSQL, penentuan akses query, dan pengujian keberhasilan database tersebut.

'''

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- 4. Relational Database & SQL

-- CREATE DATABASE finance

BEGIN;

-- Membuat table segments
CREATE TABLE segments (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

-- Membuat table countries
CREATE TABLE countries (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

-- Membuat table products
CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

-- Membuat table discountBands
CREATE TABLE discountBands (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

-- Membuat main table
CREATE TABLE mainTable (
    id SERIAL PRIMARY KEY,
    segment INT,
    country INT,
    product INT,
    discountBand INT,
	unitsSold FLOAT,
	manufacturingPrice FLOAT,
	salePrice FLOAT,
	grossSales FLOAT,
	discounts FLOAT,
	sales FLOAT,
	cogs FLOAT,
	profit FLOAT,
	date DATE,
	monthNumber INT,
	monthName VARCHAR(50),
	year INT	
);

-- Membuat SAVEPOINT
SAVEPOINT before_copy;

-- Memasukkan isi dari table segments
COPY segments(name)
FROM 'C:\tmp\segments.csv'
DELIMITER ','
CSV HEADER;

-- Memasukkan isi dari table countries
COPY countries(name)
FROM 'C:\tmp\countries.csv'
DELIMITER ','
CSV HEADER;

-- Memasukkan isi dari table products
COPY products(name)
FROM 'C:\tmp\products.csv'
DELIMITER ','
CSV HEADER;

-- Memasukkan isi dari table discountBands
COPY discountBands(name)
FROM 'C:\tmp\discountBands.csv'
DELIMITER ','
CSV HEADER;

-- Memasukkan isi dari main table
COPY mainTable(segment,
			   country,
			   product,
			   discountBand,
			   unitsSold,
			   manufacturingPrice,
			   salePrice,
			   grossSales,
			   discounts,
			   sales,
			   cogs,
			   profit,
			   date,
			   monthNumber,
			   monthName,
			   year)
FROM 'C:\tmp\mainTable.csv'
DELIMITER ','
CSV HEADER;

RELEASE SAVEPOINT before_copy;

-- Membuat 2 user baru
CREATE USER user1 WITH PASSWORD '1234'
CREATE USER user2 WITH PASSWORD '1234'

-- Memberikan grant dan revoke pada user1
GRANT SELECT ON ALL TABLES IN SCHEMA PUBLIC TO user1;
REVOKE INSERT, UPDATE, TRUNCATE, DELETE ON ALL TABLES IN SCHEMA PUBLIC FROM user1;

-- Memberikan akses seluruhnya pada user2
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA PUBLIC TO user2;

COMMIT;

-- Mengganti role
SET ROLE user1
SET ROLE user2
SET ROLE postgres

-- Menampilkan table
SELECT * FROM segments
SELECT * FROM countries
SELECT * FROM products
SELECT * FROM discountBands
SELECT * FROM mainTable

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- 5. Pengujian Database

-- No. 1a
-- Berikan tabel yang berisikan informasi total profit yang didapatkan di tiap jenis segmentasi. Jangan ambil data yang tidak diskon.
SELECT a.name as "Segment",
	   ROUND(SUM(b.profit)::numeric, 2) as "Total Profit"
FROM segments as a
JOIN mainTable as b
ON a.id = b.segment
WHERE b.discounts > 0
GROUP BY 1
ORDER BY 2 DESC;

-- No. 1b
-- Berikan tabel yang berisikan informasi rangkuman statistik yang memuat nilai rata-rata, min, dan max (dijadikan dalam kolom yang berbeda) dari Sales masing-masing negara.
SELECT a.name as "Country",
	   ROUND(AVG(b.sales)::numeric, 2) as "Average Sales",
	   MIN(b.sales) as "Minimum Sales",
	   MAX(b.sales) as "Maximum Sales"
FROM countries as a
JOIN mainTable as b
ON a.id = b.country
GROUP BY 1;

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

KESIMPULAN

Kesimpulan dari proses ini adalah setelah melakukan cleaning dan normalisasi data, data tersebut telah siap untuk dibuatkan database. Oleh karena itu, menggunakan PostgreSQL, dibuat database baru yang terdiri dari 5 tabel, yaitu main table, segment, country, product, dan discount band yang merupakan primary key dari setiap tabel.
Setelah pembuatan database dan tabel selesai, isi data dari file tabel CSV diinput ke dalam tabel-tabel tersebut. Selain itu, pada tahap ini,  diberikan pula izin akses kepada user yang telah dibuat serta melakukan pengujian database.

'''




