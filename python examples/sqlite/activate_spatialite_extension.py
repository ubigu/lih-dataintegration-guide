'''
This code creates SQlite database.

Then the code enables spatialite extension.

After that table with spatial data is created.
You can add your own data to the code at this point.

Then the created data is queried and the results
are printed to the output console.

'''


import sqlite3

# Create a SQLite database
conn = sqlite3.connect('example.db')

# Enable spatialite extension
conn.enable_load_extension(True)
conn.execute("SELECT load_extension('mod_spatialite')")

# Create a table with spatial data
conn.execute('''CREATE TABLE spatial_data (id INTEGER PRIMARY KEY,
                                            name TEXT,
                                            geom GEOMETRY);''')

# Insert some spatial data
conn.execute("INSERT INTO spatial_data (name, geom) VALUES ('Point A', GeomFromText('POINT(1 1)'));")
conn.execute("INSERT INTO spatial_data (name, geom) VALUES ('Point B', GeomFromText('POINT(2 2)'));")

# Query spatial data
result = conn.execute("SELECT name, AsText(geom) FROM spatial_data;")
for row in result:
    print(row)

# Close the connection
conn.close()
