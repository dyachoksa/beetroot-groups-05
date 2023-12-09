import sqlite3

conn = sqlite3.connect("db.sqlite3")

# create table:
print("Create customers table...")
# conn.execute("""
# CREATE TABLE customers (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   first_name VARCHAR(100) NOT NULL,
#   last_name VARCHAR(100) NOT NULL,
#   date_of_birth DATE,
#   country VARCHAR(100) NOT NULL,
#   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """)

# insert data
# print("Insert initial data...")
# data = [
#     ("Charles", "Newman", "1973-11-07", "USA"),
#     ("Isaac", "Pierce", None, "USA"),
#     ("Julie", "Jenkins", "1968-03-05", "Canada"),
# ]
# conn.executemany("""
# INSERT INTO customers (first_name, last_name, date_of_birth, country)
# VALUES (?, ?, ?, ?)
# """, data)
# conn.commit()

# select data
print("Select all customers...")
sql = "SELECT id, last_name, first_name FROM customers ORDER BY last_name, first_name;"
for row in conn.execute(sql):
    print(row)


print("Select countries and number of customers")
sql = """
SELECT
  country, count(*) AS num_of_customers 
FROM customers 
GROUP BY country 
ORDER BY country;
"""
for row in conn.execute(sql):
    print(row)
