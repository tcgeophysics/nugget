# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:52:24 2013

@author: thomascampagne

Testing stsci.imagemanip.interp2d.expand2d
"""

from GridIO import GetGeoGrid
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import interpolate
import numpy
import stsci.imagemanip.interp2d as interp2d
#from bob import sp


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

SourceMaxX = SourceOriginX + xsize * SourcePixelWidth
SourceMinY = SourceOriginY + ysize * SourcePixelHeight
print SourceOriginX, SourceMaxX, SourcePixelWidth
print SourceOriginY, SourceMinY, SourcePixelHeight
x = numpy.linspace(SourceOriginX, SourceMaxX, xsize)
y = numpy.linspace(SourceMinY, SourceOriginY, ysize)

xminTarget = SourceOriginX - xsize * SourcePixelWidth
xmaxTarget = SourceOriginX + xsize * 2 * SourcePixelWidth
ymaxTarget = SourceOriginY + ysize * -1 * SourcePixelHeight
yminTarget = SourceOriginY + ysize * 2 * SourcePixelHeight
print xminTarget, xmaxTarget, yminTarget, ymaxTarget

xTarget = numpy.linspace(xminTarget, xmaxTarget, xsize * 3)
yTarget = numpy.linspace(yminTarget, ymaxTarget, ysize * 3)

# Extrapolate array to new dimensions
#TargetArray = expand2d(SourceArray,TargetShape)

## Using scipy.interpolate.RectBivariateSpline(x,y,z)
## and scipy.interpolate.RectBivariateSpline.__call__(x,y)
#print 'here ', xsize, ysize, SourceArray.shape, x.shape, y.shape,
#MySpline = interpolate.RectBivariateSpline(y, x, SourceArray)
#TargetArray = MySpline.__call__(yTarget, xTarget)

## Using scipy.interpolate.interp2d(x, y, z, kind='linear')
## kind : linear, cubic, quintic
#MySpline = interpolate.interp2d(x, y, SourceArray, kind='cubic')
#
#TargetArray = MySpline(xTarget, yTarget)

## Using bob.sp.extrapolate_mirror
#TargetArray = numpy.zeros( (Nr,Nc) , dtype = float )
#MySpline = sp.extrapolate_mirror(SourceArray, )

## Using stsci.imagemanip.interp2d.expand2d
## Check function call
TargetArray = interp2d.expand2d (SourceArray,TargetShape)


# Plotting using pyplot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))

ax1.set_title('Source array')
im1 = ax1.imshow(SourceArray, aspect='equal', cmap=cm.jet)

ax2.set_title('Extrapolated array')
im1 = ax2.imshow(TargetArray, aspect='equal', cmap=cm.jet)

fig.show()
