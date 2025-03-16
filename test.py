import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Check for tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()

print("Tables in database:", tables)  # Should print [('users',)]
conn.close()