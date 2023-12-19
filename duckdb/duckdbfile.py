import duckdb

# This will create a new DuckDB database file named 'my_duckdb.duckdb'
# If the file already exists, it will connect to it
conn = duckdb.connect('my_duckdb.duckdb')

# Example: Create a table and insert data
conn.execute("CREATE TABLE items (id INTEGER, name VARCHAR)")
conn.execute("INSERT INTO items VALUES (1, 'Item 1'), (2, 'Item 2')")

# Commit if you've made changes
conn.commit()

# Query data
result = conn.execute("SELECT * FROM items").fetchall()
print(result)

# Close the connection
conn.close()
