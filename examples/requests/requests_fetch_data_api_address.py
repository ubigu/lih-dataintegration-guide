import requests
import geopandas as gpd

def fetch_wfs_data(url, typename):
    try:
        # Construct parameters for the WFS request
        params = {
            'service': 'WFS',
            'version': '1.0.0',
            'request': 'GetFeature',
            'typeName': typename,
            'outputFormat': 'json'  # Assuming GeoJSON response
        }

        # Send GET request to the WFS endpoint
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error if the request fails

        # Parse GeoJSON response into a Python dictionary
        data = response.json()

        # Convert GeoJSON features to GeoDataFrame
        gdf = gpd.GeoDataFrame.from_features(data['features'])

        return gdf

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
url = "https://paituli.csc.fi/geoserver/paituli/wfs"
typename = "paituli:tike_kuntienVaesto_2022"

# Fetch WFS data and convert to GeoDataFrame
gdf = fetch_wfs_data(url, typename)

# Iterate over the rows of the GeoDataFrame
for index, row in gdf.iterrows():
    # Access values of the desired columns for each row
    nimi = row['nimi']  # Assuming 'nimi' is one of the columns
    vaki = row['vaesto']  # Assuming 'other_column' is another column
    
    # Print the data
    print(f"Kuntanimi: {nimi}")     
    print(f"Väestö: {vaki}")