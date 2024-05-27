import pandas as pd
import geopandas as gpd

# Non-geospatial DataFrame
non_geospatial_data = pd.DataFrame({
    'store_id': [1, 2, 3],
    'sales_revenue': [10000, 15000, 8000],
    'average_transaction_value': [50, 60, 40],
    # Add more non-geospatial columns as needed
})

# Geospatial GeoDataFrame
# Assuming you have a shapefile or GeoJSON file containing store locations
# Replace 'stores.shp' with your actual file path
geospatial_data = gpd.read_file('stores.shp')

# Assuming the 'store_id' column exists in both DataFrames and can be used for joining
# Merge the two DataFrames based on the 'store_id' column
merged_data = pd.merge(non_geospatial_data, geospatial_data, on='store_id', how='inner')

# Print the merged DataFrame
print(merged_data)