'''
This is an example where ogr is used to get some basic
information about vector file.

The information is printed out in output console.

The code prints the names of all columns from the vector file. 

Note! Remember to replace the vector_path with the
path to your vector file.

'''

from osgeo import ogr

# Path to the GeoPackage file
vector_file = "path/to/your/file"

# Open the GeoPackage
extension = "your filetype"     #Replace with the correct file extension ("GPKG", "ESRI Shapefile", ect.)
driver = ogr.GetDriverByName(extension)
dataset = driver.Open(vector_file)

if dataset is None:
    print("Failed to open the file.")
else:
    # Get the layer from the GeoPackage
    layer = dataset.GetLayer()

    # Get the layer's schema
    layer_defn = layer.GetLayerDefn()

    # Get column names
    column_names = [layer_defn.GetFieldDefn(i).GetName() for i in range(layer_defn.GetFieldCount())]

    # Print column names
    print("Column names in the file:")
    print(column_names)

    # Close the dataset
    dataset = None