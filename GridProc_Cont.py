# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:07:21 2013

@author: thomascampagne

Working code of upward continuation
Edge effect in output
"""

from numpy import linspace ,zeros, real
from scipy.fftpack import fft2 , fftfreq, ifft2
from cmath import pi, exp
from math import pow, sqrt
from GridIO import GetGeoGrid, CreateGeoGrid
from GridPlot import ArrayPlot

FileName       =   'data/can1k_mag_NAD83_crop02_UTM.tiff'
TargetFileName =   'data/can1k_mag_NAD83_crop02_UTM_cont.tiff'

#FileName       =   'data/CAN_Bouguer_NAD83_crop02_UTM.tiff'
#TargetFileName =   'data/CAN_Bouguer_NAD83_crop02_UTM_cont.tiff'


zp = -1000 # zp < 0 moves away from sources

# Import data
SourceOriginX, SourceOriginY, SourcePixelWidth, SourcePixelHeight, Projection, Bands, \
SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)

# get Array info
TempArray = SourceArray
TempArrayShape = TempArray.shape
Nc = TempArrayShape [1] #x length
Nr = TempArrayShape [0] #y length

# assign some real spatial co-ordinates to the grid points   
# first define the edge values
x_min = SourceOriginX
x_max = SourceOriginX + xsize * SourcePixelWidth
y_min = SourceOriginY
y_max = SourceOriginY + ysize * SourcePixelHeight

# then create some empty 2d arrays to hold the individual cell values
x_array = zeros( TempArrayShape , dtype = float )
y_array = zeros( TempArrayShape , dtype = float )

# now fill the arrays with the associated values
for row , y_value in enumerate(linspace (y_min , y_max , num = Nr) ):

  for column , x_value in enumerate(linspace (x_min , x_max , num = Nc) ):

    x_array[row][column] = x_value
    y_array[row][column] = y_value

# now for any row,column pair the x_array and y_array hold the spatial domain
# co-ordinates of the associated point in some_data_grid

# now use the fft to transform the data to the wavenumber domain
TempArray_wavedomain = fft2(TempArray)

# now we can use fftfreq to give us a base for the wavenumber co-ords
# this returns [0.0 , 1.0 , 2.0 , ... , 62.0 , 63.0 , -64.0 , -63.0 , ... , -2.0 , -1.0 ]
n_value = fftfreq( Nr , (1.0 / float(Nr) ) )
m_value = fftfreq( Nc , (1.0 / float(Nc) ) )

# now we can initialize some arrays to hold the wavenumber co-ordinates of each cell
kx_array = zeros( TempArrayShape , dtype = float )
ky_array = zeros( TempArrayShape , dtype = float )
TempArray_wavedomain_proc = zeros( TempArrayShape , dtype = complex )
# before we can calculate the wavenumbers we need to know the total length of the spatial
# domain data in x and y. This assumes that the spatial domain units are metres and
# will result in wavenumber domain units of radians / metre.
x_length = xsize * SourcePixelWidth
y_length = ysize * SourcePixelHeight

# now the loops to calculate the wavenumbers
for row in xrange(Nr):
    
    for column in xrange(Nc):
        
        kx_array[row][column] = ( 2.0 * pi * n_value[column] ) / x_length
        ky_array[row][column] = ( 2.0 * pi * n_value[row] ) / y_length

# now for any row,column pair kx_array , and ky_array will hold the wavedomain coordinates
# of the correspoing point in some_data_wavedomain
        kw = sqrt(pow(kx_array[row][column],2)+pow(ky_array[row][column],2))
        
        TempArray_wavedomain_proc [row][column] = TempArray_wavedomain [row][column] * exp(kw*zp)


TempArray_proc = ifft2(TempArray_wavedomain_proc)
TempArray_proc = real(TempArray_proc)
#print amax(TempArray_proc)
#print amin(TempArray_proc)
#print NDV

TargetArray = TempArray_proc
TargetType = SourceType
NDV = -99999

# Plot array
ArrayPlot(SourceArray, TargetArray,SourceOriginX, SourceOriginY, \
SourcePixelWidth, SourcePixelHeight, SameCB=True)

# Export
CreateGeoGrid(FileName, TargetFileName, xsize, ysize, TargetType, TargetArray, NDV)