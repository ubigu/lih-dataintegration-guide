from bs4 import BeautifulSoup

# Sample XML data (replace this with your actual XML file)
xml_data = """
<geospatial_data>
    <point_of_interest>
        <name>Eiffel Tower</name>
        <latitude>48.8584</latitude>
        <longitude>2.2945</longitude>
    </point_of_interest>
    <point_of_interest>
        <name>Statue of Liberty</name>
        <latitude>40.6892</latitude>
        <longitude>-74.0445</longitude>
    </point_of_interest>
    <point_of_interest>
        <name>Sydney Opera House</name>
        <latitude>-33.8568</latitude>
        <longitude>151.2153</longitude>
    </point_of_interest>
</geospatial_data>
"""

# Parse the XML data using BeautifulSoup
soup = BeautifulSoup(xml_data, "xml")

# Extract information from each point of interest
points_of_interest = []
for poi in soup.find_all("point_of_interest"):
    name = poi.find("name").text
    latitude = float(poi.find("latitude").text)
    longitude = float(poi.find("longitude").text)
    points_of_interest.append({"name": name, "latitude": latitude, "longitude": longitude})

# Print the extracted data
for poi in points_of_interest:
    print("Name:", poi["name"])
    print("Latitude:", poi["latitude"])
    print("Longitude:", poi["longitude"])
    print()