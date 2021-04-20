import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=db1 user=mac port=1234")
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM sch1.users")

# Retrieve query results
records = cur.fetchall()