import geopandas as gpd
from shapely.geometry import Point
from bs4 import BeautifulSoup

# Sample XML data with additional, non-useful values
xml_data = """
<geospatial_data>
    <point_of_interest>
        <name>Eiffel Tower</name>
        <latitude>48.8584</latitude>
        <longitude>2.2945</longitude>
        <spatial_reference>EPSG:4326</spatial_reference>
        <additional_info>
            <creator>Gustave Eiffel</creator>
            <year_built>1889</year_built>
        </additional_info>
    </point_of_interest>
    <point_of_interest>
        <name>Statue of Liberty</name>
        <latitude>40.6892</latitude>
        <longitude>-74.0445</longitude>
        <spatial_reference>EPSG:4326</spatial_reference>
        <additional_info>
            <creator>Frédéric Auguste Bartholdi</creator>
            <year_built>1886</year_built>
        </additional_info>
    </point_of_interest>
    <point_of_interest>
        <name>Sydney Opera House</name>
        <latitude>-33.8568</latitude>
        <longitude>151.2153</longitude>
        <spatial_reference>EPSG:4326</spatial_reference>
        <additional_info>
            <creator>Jørn Utzon</creator>
            <year_built>1973</year_built>
        </additional_info>
    </point_of_interest>
</geospatial_data>
"""

def xml_to_gpkg(xml_data, output_gpkg):
    # Parse the XML data using BeautifulSoup
    soup = BeautifulSoup(xml_data, "xml")
    
    # Extract useful information from each point of interest
    points_of_interest = []
    for poi in soup.find_all("point_of_interest"):
        name = poi.find("name").text
        latitude = float(poi.find("latitude").text)
        longitude = float(poi.find("longitude").text)
        spatial_reference = poi.find("spatial_reference").text
        # Only extracting useful information
        points_of_interest.append({
            "name": name,
            "latitude": latitude,
            "longitude": longitude,
            "spatial_reference": spatial_reference
        })

    # Create a GeoDataFrame
    geometry = [Point(poi["longitude"], poi["latitude"]) for poi in points_of_interest]
    names = [poi["name"] for poi in points_of_interest]
    gdf = gpd.GeoDataFrame({'name': names, 'geometry': geometry}, crs="EPSG:4326")

    # Save the GeoDataFrame to a GeoPackage
    gdf.to_file(output_gpkg, layer='points', driver="GPKG")

    print(f"GeoPackage {output_gpkg} created successfully.")

'''
If you want to save the result .gpkg to you file explorer then run following code 

# Create the GeoPackage from the XML data
xml_to_gpkg(xml_data, "points_of_interest.gpkg")

'''