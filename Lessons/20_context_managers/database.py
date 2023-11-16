class Database:
    def __init__(self, dsn) -> None:
        self.dsn = dsn

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def open(self):
        print("Opening connection to the database:", self.dsn)
        return self
    
    def close(self):
        print("Closing the database connection")
    
    def run_query(self, query):
        print("Executing query to the database:", query)


# 'Plain' usage:
db = Database("host=127.0.0.1 name=app")

# 1. open connection
db.open()
# 2. run query(ies)
db.run_query("SELECT ALL USERS")
# 3. close connection
db.close()

print()

# 'Context manager' usage
with Database("host=127.0.0.1 name=app") as db1:
    db1.run_query("FIND USER BY EMAIL")
    db1.run_query("UPDATE USER")

print()

# We can even use several connections to different databases
try:
    with Database("database #1") as d1, Database("database #2") as d2:
        d1.run_query("SELECT ALL ARTICLES")
        d2.run_query("WRITE STATS")
except:
    pass
