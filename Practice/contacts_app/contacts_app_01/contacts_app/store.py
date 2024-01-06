import sqlite3

from contacts_app.models import Customer


class DatabaseStore:
    def __init__(self, db_name = "db.sqlite3") -> None:
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

    def get_customers(self):
        customers = []

        query = """
SELECT id, last_name, first_name, email, date_of_birth, created_at
FROM customers ORDER BY first_name, last_name;
"""
        result = self.conn.execute(query)
        for row in result:
            customers.append(Customer(
                first_name=row[2],
                last_name=row[1],
                email=row[3],
                date_of_birth=row[4],
                customer_id=row[0]
            ))
        
        return customers
    
    def insert_customer(self, customer: "Customer"):
        query = """
INSERT INTO customers (first_name, last_name, email, date_of_birth)
VALUES (:first_name, :last_name, :email, :date_of_birth)
"""
        data = {
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
            "date_of_birth": customer.date_of_birth,
        }
        self.conn.execute(query, data)
        self.conn.commit()

    def init_store(self):
        self.conn.executescript("""
CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  date_of_birth DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_customer_email ON customers (email);
""")

        self.conn.executescript("""
CREATE TABLE addresses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  city VARCHAR NOT NULL,
  post_code VARCHAR NOT NULL,
  address VARCHAR NOT NULL,
  is_shipping BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE
);

CREATE INDEX idx_address_customer_id ON addresses (customer_id);
CREATE INDEX idx_address_post_code ON addresses (post_code);
""")
