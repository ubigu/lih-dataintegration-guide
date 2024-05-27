'''
This code parses html address by using beautiful soup.
The parsed file is then saved as geopackage by using geopandas.

This code only parses latitude, longitude and name from the XML.
Latitude and longitude are essential for geopackage.

You can alter the code and parse what you want. See latitude,
longitude and name for example.

Note! Remember to replace url with the url address that you desire
to use.
Also remember to define where and with what name you want to output
geopackage to be saved.

'''

import requests
import geopandas as gpd
from bs4 import BeautifulSoup
from shapely.geometry import Point

def parse_html_to_geopackage(url, output_gpkg):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    
    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data from the HTML
    data = []
    for feature in soup.find_all('div', class_='feature'):
        # Extract name, latitude, and longitude elements
        name = feature.find('p', class_='name').text
        lat = float(feature.find('p', class_='latitude').text)
        lon = float(feature.find('p', class_='longitude').text)

        # Create a dictionary for each feature
        data.append({'name': name, 'geometry': Point(lon, lat)})
    
    # Convert the data into a GeoDataFrame
    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")
    
    # Save the GeoDataFrame to a GeoPackage
    gdf.to_file(output_gpkg, layer='features', driver="GPKG")
    
    print(f"GeoPackage saved to {output_gpkg}")

# Example usage
url = "https://example.com/data.html"  # Replace with the actual URL
output_gpkg = "output.gpkg"  # Path to the output GeoPackage

parse_html_to_geopackage(url, output_gpkg)