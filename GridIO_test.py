# -*- coding: utf-8 -*-
"""
TC, Nov 19, 2013
Importing a grid with GDAL and converting its data band to a 2D numpy array
Exporting a 2D numpy array to a grid with same properties and stats
"""

import gdal, numpy
from gdalconst import *

# register all of the drivers
#gdal.AllRegister()

# open the raster
inDs = gdal.Open('can1k_NAD83_crop01.tiff', GA_ReadOnly)

# get raster size
rows = inDs.RasterYSize
cols = inDs.RasterXSize
bands = inDs.RasterCount

# Set NoData Value
inBand = inDs.GetRasterBand(1)
ndv = inBand.GetNoDataValue()
print 'ndv =', ndv
#band.SetNoDataValue(ndv)

# Get Statistics
inStats = inBand.ComputeStatistics(0)
print 'inStats =',inStats
#inType = gdal.GetDataTypeName(inBand.DataType) # Remove prefix 'GDT_'
inType = inDs.GetRasterBand(1).DataType
print 'inBand Type=',gdal.GetDataTypeName(inType)


# read in band as array
bandList = []
inBand.GetNoDataValue()
data = inBand.ReadAsArray(0, 0, cols, rows)
print 'inData ', type(data), data.shape

# Modify array
data2 = data + 1000
print 'outData ', type(data2), data2.shape
print 'outData max/min',numpy.max(data2), numpy.min(data2)

# Creat output raster
#driver = inDs.GetDriver()
driver = gdal.GetDriverByName('GTiff')

# Create output type name
#outType = 'GDT_' + inType
outType = inType
print 'outBand Type=',gdal.GetDataTypeName(outType)

#print driver
outDs = driver.Create("can1k_NAD83_crop01_modified.tiff", cols, rows, 1, outType)
if outDs is None:
    print 'Could not create output file'
    sys.exit(1)

# georeference the image and set the projection
print 'inGeoTransform ', inDs.GetGeoTransform()
outDs.SetGeoTransform(inDs.GetGeoTransform())
print 'outGeoTransform ', outDs.GetGeoTransform()
print 'Projection ', inDs.GetProjection()
outDs.SetProjection(inDs.GetProjection())

# create output band
outBand = outDs.GetRasterBand(1)
outData = data2

# write the data
outBand.WriteArray(outData)

# Get Statistics
outStats = outBand.ComputeStatistics(0)
print 'outStats =',outStats

# flush data to disk, set the NoData value and calculate stats
outBand.FlushCache()
#outBand.SetNoDataValue(ndv)

del outData

