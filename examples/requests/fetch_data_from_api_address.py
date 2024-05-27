'''
This is an example where requests are used to
fecth WFS data from url address.

This code prints to the output console available
WFS layers. Then user is able to select the desired
layer. After selection the available columns are
printed on the output console.


Note! Remember to replace the url with the address
to your WFS API.

'''

import requests
import geopandas as gpd
from owslib.wfs import WebFeatureService

def list_wfs_layers(url):
    wfs = WebFeatureService(url=url, version='1.0.0')
    layers = list(wfs.contents)
    print("Available WFS Layers:")
    for i, layer in enumerate(layers):
        print(f"{i + 1}. {layer}")
    return layers

def fetch_layer_schema(wfs_url, typename):
    wfs = WebFeatureService(url=wfs_url, version='1.0.0')
    schema = wfs.get_schema(typename)
    return schema['properties']

def fetch_wfs_data(url, typename):
    try:
        params = {
            'service': 'WFS',
            'version': '1.0.0',
            'request': 'GetFeature',
            'typeName': typename,
            'outputFormat': 'json'
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        gdf = gpd.GeoDataFrame.from_features(data['features'])
        return gdf

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
wfs_url = "Enter the WFS URL"

# List available layers
layers = list_wfs_layers(wfs_url)

# Select a layer (user input)
layer_index = int(input("Enter the number of the layer you want to inspect: ")) - 1
selected_layer = layers[layer_index]

# Print all available columns for the selected layer
print(f"\nAvailable columns for layer '{selected_layer}':")
columns = fetch_layer_schema(wfs_url, selected_layer)
for column in columns:
    print(column)

# Fetch WFS data and convert to GeoDataFrame
gdf = fetch_wfs_data(wfs_url, selected_layer)

# Iterate over the rows of the GeoDataFrame
for index, row in gdf.iterrows():
    # Print all columns for each row
    for column in columns:
        print(f"{column}: {row.get(column, 'N/A')}")
    print("-" * 20)  # Separator for readability
