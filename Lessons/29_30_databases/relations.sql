CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE addresses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  address TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE
);

INSERT INTO customers (first_name, last_name, email)
  VALUES 
    ("Julie", "Jenkins", "julie.jenkins@example.com"),
    ("Mattie", "Campbell", "mattie.campbell@example.com");

INSERT INTO addresses (customer_id, address)
  VALUES
    (1, "7781 Taylor St"),
    (1, "1512 Oak Lawn Ave"),
    (2, "4438 Cackson St");

-- select all customers
SELECT * FROM customers;

-- select all customers (restricted to first and last name) with address
SELECT
  c.first_name,
  c.last_name,
  a.address
FROM customers AS c
  INNER JOIN addresses AS a ON a.customer_id = c.id;
