'''
This is an example where we connect to
PostgreSQL database by using psycopg2.

This example selects all the data in one table
and prints it.

Note! You have to define dbname, user,
password, host, post and the desired table from 
the database in order to use this code.

'''

import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM your_table")

# Fetch the results
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and the connection
cur.close()
conn.close()
