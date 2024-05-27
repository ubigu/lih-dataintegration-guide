'''
This is an example where we connect to
PostgreSQL database by using psycopg2.

This example selects all the data in one table
and prints it.

Note! You have to define database, host, user and
password.

'''

import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    database="database_name"  # Your database name
    host="localhost",  # Your host
    user="username",   # Your username
    password="password",  # Your password
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute a query
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()