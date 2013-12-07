# -*- coding: utf-8 -*-
"""
TC, Nov 22, 2013
Importing a grid with GDAL and converting its data band to a 2D numpy array
Exporting a 2D numpy array to a grid with same properties and stats
"""

import gdal, osr, sys
from gdalconst import GA_ReadOnly



def GetGeoGrid(FileName):
    print '\nImporting'
    # Open source file
    SourceDS = gdal.Open(FileName, GA_ReadOnly)
    # Count number of data bands
    Bands = SourceDS.RasterCount
    if Bands > 1:
        print str(Bands) + ' bands detected.\n Multiple bands not supported.'
        # need to select proper data band
        sys.exit(1)
    # Get the first band
    SourceBand = SourceDS.GetRasterBand(1)
    # Compute first band stats
    SourceStats = SourceBand.ComputeStatistics(0)
    print 'Source [ Min, Max, Mean, Std Dev ] =\n', SourceStats
    # Get no data value
    NDV = SourceBand.GetNoDataValue()
    # Get raster size
    xsize = SourceDS.RasterXSize
    ysize = SourceDS.RasterYSize
    # Get the geographic transformation
    GeoT = SourceDS.GetGeoTransform()
    # Get raster origin and resolution
    SourceOriginX = GeoT[0]
    SourceOriginY = GeoT[3]
    SourcePixelWidth = GeoT[1]
    SourcePixelHeight = GeoT[5]
    print 'Upper left corner (x , y) = (',SourceOriginX,', ',SourceOriginY,',)'
    print 'Pixel dimension (width, height) = (',SourcePixelWidth,', ',SourcePixelHeight,',)'
    # Get the projection
    Projection = osr.SpatialReference()
    Projection.ImportFromWkt(SourceDS.GetProjectionRef())
    print 'Source Projection is\n',SourceDS.GetProjection()
    # Get the band data type
    SourceType = SourceBand.DataType
    print 'Source Band Type=',gdal.GetDataTypeName(SourceType)
    # Write the raster band as a numpy array
    SourceArray = SourceBand.ReadAsArray(0, 0, xsize, ysize)
    print 'Source Array type ', type(SourceArray),'\nSource Array size ', SourceArray.shape
    return  SourceOriginX, SourceOriginY, SourcePixelWidth, SourcePixelHeight, Projection, \
    Bands, SourceType, NDV, xsize, ysize, SourceArray, SourceStats
# To use: 
# SourceOriginX, SourceOriginY, SourcePixelWidth, SourcePixelHeight, Projection, \
#    Bands, SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)
    
    
def CreateGeoGrid(FileName, TargetFileName, xsize, ysize, TargetType, TargetArray, NDV):
    print '\nExporting'
    # Open source file
    SourceDs = gdal.Open(FileName, GA_ReadOnly)
    # Get source file driver
    driver = SourceDs.GetDriver()
    # Get source file band data type
    #TargetType = SourceDs.GetRasterBand(1).DataType
    print 'Target Band Type=',gdal.GetDataTypeName(TargetType)
    # Get source first band no data value
    #NDV = SourceDS.GetRasterBand(1).GetNoDataValue()
    # Create target raster file of same dimension and band data type as source file
    TargetDs = driver.Create(TargetFileName, xsize, ysize, 1, TargetType)
    if TargetDs is None:
        print 'Could not create target file'
        sys.exit(1)
    # Apply same geographic transformation as source to target file
    TargetDs.SetGeoTransform(SourceDs.GetGeoTransform())
    # Apply same projection as source to target file
    TargetDs.SetProjection(SourceDs.GetProjection())
    # Get target  first raster band (empty at this point)
    TargetBand = TargetDs.GetRasterBand(1)
    # Write the numpy array to target band
    TargetWrite = TargetBand.WriteArray(TargetArray)
    if TargetWrite is None:
        print 'Could not write to target file'
        sys.exit(1)
    # Flush data to disk, set the NoData value and calculate stats
    TargetBand.FlushCache()
    # Set default no data value
    if NDV is None:
        NDV = -99999
    TargetBand.SetNoDataValue(NDV)
    # Compute first band stats
    TargetStats = TargetBand.ComputeStatistics(0)
    print 'Target [ Min, Max, Mean, Std Dev ] =\n', TargetStats
    del TargetArray 
    del TargetStats
    return 0
# To use: 
# CreateGeoGrid(FileName, TargetFileName, xsize, ysize, TargetType, TargetArray)
# Return 0 if successful

