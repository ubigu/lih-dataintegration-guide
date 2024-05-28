'''
This code parses local XML file by using beautiful soup.
The parsed file is then saved as geopackage by using geopandas.

This code only parses latitude, longitude and name from the XML.
Latitude and longitude are essential for geopackage.

You can alter the code and parse what you want. See latitude,
longitude and name for example.

Note! Remember to replace xml_file with your XML file path.
Also remember to define where and with what name you want to output
geopackage to be saved.

'''

import geopandas as gpd
from bs4 import BeautifulSoup
from shapely.geometry import Point

def parse_xml_to_geopackage(xml_file, output_gpkg):
    # Read the local XML file
    with open(xml_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Parse the XML content with Beautiful Soup
    soup = BeautifulSoup(content, 'xml')
    
    # Extract data from the XML
    data = []
    for feature in soup.find_all('feature'):
        # Extract latitude, longitude, and name elements
        lat = float(feature.find('latitude').text)
        lon = float(feature.find('longitude').text)
        name = feature.find('name').text

        # Create a dictionary for each feature
        data.append({'name': name, 'geometry': Point(lon, lat)})
    
    # Convert the data into a GeoDataFrame
    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")
    
    # Save the GeoDataFrame to a GeoPackage
    gdf.to_file(output_gpkg, layer='features', driver="GPKG")
    
    print(f"GeoPackage saved to {output_gpkg}")

# Example usage
xml_file = "data.xml"
output_gpkg = "output.gpkg"

parse_xml_to_geopackage(xml_file, output_gpkg)
