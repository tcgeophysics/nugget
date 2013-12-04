# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:52:24 2013

@author: thomascampagne

Testing stsci.imagemanip.interp2d.expand2d
"""

from GridIO import GetGeoGrid
import matplotlib.pyplot as plt
from matplotlib import cm
from stsci_imagemanip.interp2d import expand2d



FileName       =   'data/can1k_mag_NAD83_crop02_UTM.tiff'
TargetFileName =   'data/can1k_mag_NAD83_crop02_UTM_contpad.tiff'

# Import data
SourceOriginX, SourceOriginY, SourcePixelWidth, SourcePixelHeight, Projection, Bands, \
SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)

# extrapolate
SourceShape = SourceArray.shape
print 'Source shape = ', SourceShape
Col = SourceShape [1] #x length
Row = SourceShape [0] #y length
TempArray = expand2d(SourceArray,(Col*2, Row*2))

print 'Expand2d shape = ', TempArray.shape

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))

ax1.set_title('Source array')
im1 = ax1.imshow(SourceArray, aspect='equal', cmap=cm.jet)

ax2.set_title('Extrapolated array')
im1 = ax2.imshow(TempArray, aspect='equal', cmap=cm.jet)

fig.show()

# 
#TargetArray = TempArray_proc
#TargetType = SourceType
#NDV = -99999

## Plot array
#ArrayPlot(SourceArray, TargetArray,SourceOriginX, SourceOriginY, \
#SourcePixelWidth, SourcePixelHeight, SameCB=True)

## Export
#CreateGeoGrid(FileName, TargetFileName, xsize, ysize, TargetType, TargetArray, NDV)