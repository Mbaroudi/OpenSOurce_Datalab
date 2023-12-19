import duckdb

# Connect to DuckDB. This will create a new database file if it doesn't exist
conn = duckdb.connect('my_duckdb.duckdb')

# Create a table and insert data
conn.execute("""
CREATE TABLE my_table (
    id INT,
    name VARCHAR,
    quantity INT,
    price DECIMAL
)
""")

conn.execute("""
INSERT INTO my_table (id, name, quantity, price) VALUES
(1, 'Apple', 10, 0.50),
(2, 'Orange', 20, 0.30),
(3, 'Banana', 15, 0.20),
(4, 'Grapes', 5, 1.00)
""")

# Commit changes and close the connection
conn.commit()
conn.close()
