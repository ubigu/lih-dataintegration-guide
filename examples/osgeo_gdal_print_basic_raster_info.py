from osgeo import gdal

# Path to the raster file
raster_path = "path/to/your/raster/file.tif"

# Open the raster dataset
dataset = gdal.Open(raster_path)

if dataset is None:
    print("Failed to open the raster dataset.")
else:
    # Get the number of bands in the raster dataset
    num_bands = dataset.RasterCount
    print("Number of bands:", num_bands)

    # Get the raster size (width and height)
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    print("Raster size (width x height):", width, "x", height)

    # Get the geotransform parameters (georeferencing information)
    geotransform = dataset.GetGeoTransform()
    print("Geotransform parameters:", geotransform)

    # Get the spatial reference system (SRS)
    srs = dataset.GetProjection()
    print("Spatial Reference System:", srs)

    # Close the raster dataset
    dataset = None