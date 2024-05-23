import sqlite3

# Connect to a SQLite database (or create it if it doesn't exist)
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
