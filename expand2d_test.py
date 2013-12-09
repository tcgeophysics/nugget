# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:52:24 2013

@author: thomascampagne

Testing stsci.imagemanip.interp2d.expand2d
"""

from GridIO import GetGeoGrid
import matplotlib.pyplot as plt
from matplotlib import cm
from interp2d import expand2d




FileName       =   'data/can1k_mag_NAD83_crop02_UTM.tiff'
TargetFileName =   'data/can1k_mag_NAD83_crop02_UTM_contpad.tiff'

# Import data
SourceOriginX, SourceOriginY, SourcePixelWidth, SourcePixelHeight, Projection, Bands, \
SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)

# extrapolate 2D array using expand2d which uses bilinearinter
# expand2d(image, outputsize)
# This function expands an input 2D data array to larger dimensions using bilinear interpolation.
# Parameters :
#     image : ndarray
#             Input image as numpy array
#     outputsize : tuple
#             Shape tuple describing the size of the output image
# Returns :
#     newimage : ndarray
#             bilinearly interpolated array with shape specified by outputsize parameter

# Calculate output array shape
SourceShape = SourceArray.shape
print 'Source shape = ', SourceShape
TargetShape = (SourceShape [0] * 2, SourceShape [1] * 2) 
print 'Target shape = ', TargetShape

# Extrapolate array to new dimensions
TargetArray = expand2d(SourceArray,TargetShape)

# Plotting using pyplot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))

ax1.set_title('Source array')
im1 = ax1.imshow(SourceArray, aspect='equal', cmap=cm.jet)

ax2.set_title('Extrapolated array')
im1 = ax2.imshow(TargetArray, aspect='equal', cmap=cm.jet)

fig.show()
