'''
This is an example where geopandas is to perform
intersection operation.

The code prints the result intersection.

Note! In this example the sample data is created within the code.
If you want to replace the data with vector files, then replace
data1 and data2 with file path to your data.

'''



import geopandas as gpd
from shapely.geometry import Point

# Create GeoDataFrames with sample data
data1 = {'geometry': [Point(0, 0).buffer(1), Point(1, 1).buffer(1.5)]}
data2 = {'geometry': [Point(0.5, 0.5).buffer(1), Point(1.5, 1.5).buffer(1)]}
gdf1 = gpd.GeoDataFrame(data1)
gdf2 = gpd.GeoDataFrame(data2)

# Perform the intersection operation
intersection = gpd.overlay(gdf1, gdf2, how='intersection')

# Print the result
print(intersection)