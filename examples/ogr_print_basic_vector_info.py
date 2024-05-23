from osgeo import ogr

# Path to the GeoPackage file
gpkg_file = "path/to/your/file.gpkg"

# Open the GeoPackage
driver = ogr.GetDriverByName("GPKG")
dataset = driver.Open(gpkg_file)

if dataset is None:
    print("Failed to open the GeoPackage.")
else:
    # Get the layer from the GeoPackage
    layer = dataset.GetLayer()

    # Loop through each feature in the layer and print its attributes
    print("Features in the GeoPackage:")
    for feature in layer:
        # Get the attributes of the feature
        attributes = feature.items()

        # Print the attributes
        print(attributes)

    # Close the dataset
    dataset = None