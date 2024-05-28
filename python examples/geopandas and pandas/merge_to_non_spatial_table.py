'''
This is an example where geopandas and pandas are
used to merge data.

The code prints the result dataframe.

Note! In this example the sample data is created within the code.
If you want to replace the data with vector files, then replace
vehicle_locations and taxi_information with file path to your data.
You can also alter the names.

'''

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Simulated real-time vehicle location data (geospatial)
vehicle_locations = gpd.GeoDataFrame({
    'vehicle_id': [101, 102, 103],
    'timestamp': ['2024-04-09 08:00:00', '2024-04-09 08:15:00', '2024-04-09 08:30:00'],
    'geometry': [Point(-74.0060, 40.7128), Point(-73.9857, 40.7484), Point(-74.0059, 40.7127)],
    # Add more location-related attributes if available
}, crs='EPSG:4326')  # Assuming WGS84 coordinate reference system

# Simulated taxi information data (non-geospatial)
taxi_info = pd.DataFrame({
    'vehicle_id': [101, 102, 103],
    'license_plate': ['ABC123', 'DEF456', 'GHI789'],
    'driver_name': ['John Smith', 'Jane Smith', 'Mike Smith'],
    'vehicle_model': ['Toyota Corolla', 'Opel Astra', 'Ford Focus'],
    'year_of_manufacture': [2018, 2019, 2020],
    # Add more non-geospatial attributes as needed
})

# Assuming there's a common identifier like 'vehicle_id' between the two datasets
# Merge the GeoDataFrame with the DataFrame based on the 'vehicle_id' column
merged_data = pd.merge(vehicle_locations, taxi_info, on='vehicle_id', how='inner')

# Print the merged data
print(merged_data)