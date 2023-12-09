-- SQLite

-- DDL: Data Definition Language
CREATE TABLE customers (
  -- id SERIAL PRIMARY, -- For PostgreSQL
  id INTEGER PRIMARY KEY AUTOINCREMENT,  -- SQLite specific
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  date_of_birth DATE,
  country VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- DML: Data Manipulation Language
INSERT INTO customers (first_name, last_name, date_of_birth, country)
  VALUES 
    ("Charles", "Newman", "1973-11-07", "USA"),
    ("Isaac", "Pierce", NULL, "USA"),
    ("Julie", "Jenkins", "1968-03-05", "Canada");


-- DQL: Data Query Language
SELECT * FROM customers;
SELECT * FROM customers WHERE date_of_birth IS NOT NULL;
SELECT * FROM customers WHERE country = "Canada";
SELECT first_name, last_name FROM customers WHERE country = "USA";
SELECT (first_name || " " || last_name) AS full_name FROM customers;

SELECT id, last_name, first_name FROM customers ORDER BY last_name, first_name;

SELECT
  country, count(*) AS num_of_customers 
FROM customers 
GROUP BY country 
ORDER BY country;
