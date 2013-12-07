# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:36:16 2013

@author: thomascampagne
"""

from GridIO import GetGeoGrid
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import percentile


FileName       =   'data/can1k_mag_NAD83_crop02_UTM.tiff'

SourceOriginX, SourceOriginY, SourcePixelWidth, SourcePixelHeight, Projection, Bands, \
SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)

SourceArrayShape = SourceArray.shape

   

xsize = SourceArrayShape [1] #x length
ysize = SourceArrayShape [0] #y length

xmin = SourceOriginX
xmax = SourceOriginX + xsize * SourcePixelWidth
ymax = SourceOriginY + ysize * SourcePixelHeight
ymin = SourceOriginY 

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))

ax1.set_title('Source array')
im1 = ax1.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
fig.colorbar(im1, ax=ax1, shrink=0.9)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

SourceArray = SourceArray * 10
ax2.set_title('Source array')
im2 = ax2.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
fig.colorbar(im2, ax=ax2, shrink=0.9)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)


###################################
#fig = plt.figure(figsize=(16,6))
#fig.suptitle('Upward continuation', fontsize=16)
#
#plt.subplot(121)
#plt.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
##plt.axis([xmin, xmax, ymin, ymax])
#plt.title("Source array")
#cb = plt.colorbar()
#cb.set_label('nT or mGal')
#
#plt.subplot(122)
#plt.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
#plt.title("Target array")
#cb = plt.colorbar()
#cb.set_label('Processed unit')
    

fig.show()