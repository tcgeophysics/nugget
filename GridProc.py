# -*- coding: utf-8 -*-
"""
TC, Nov 29, 2013
Suite of 2D filters to process 2D numpy arrays from GridIO.py
"""
from numpy import linspace ,zeros, real
from scipy.fftpack import fft2 , fftfreq, ifft2, fftshift
from cmath import pi, exp
from math import pow, sqrt, cos, sin
from GridIO import GetGeoGrid, CreateGeoGrid

# IO functions: 
# GeoT, Projection, Bands, SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)
# CreateGeoGrid(FileName, TargetFileName, xsize, ysize, TargetType, TargetArray)
# Return 0 if successful





def PrepArray2Fourier (xsize, ysize, SpatialArray, ArrayOriginX, \
ArrayOriginY, ArrayResolutionX, ArrayResolutionY):
        
    # Get Array info
    SpatialArrayShape = SpatialArray.shape
    Nc = SpatialArrayShape [1] #x length
    Nr = SpatialArrayShape [0] #y length
    
    # assign some real spatial co-ordinates to the grid points   
    # first define the edge values

    # then create some empty 2d arrays to hold the individual cell values
    x_array = zeros( SpatialArrayShape , dtype = float )
    y_array = zeros( SpatialArrayShape , dtype = float )
    
    # now fill the arrays with the associated values
    for row , y_value in enumerate(linspace (ArrayOriginY , ArrayOriginY + \
    ysize * ArrayResolutionY , num = Nr) ):
        
        for column , x_value in enumerate(linspace (ArrayOriginX , \
        ArrayOriginX + xsize * ArrayResolutionX , num = Nc) ):

            x_array[row][column] = x_value
            y_array[row][column] = y_value
            
            # now for any row,column pair the x_array and y_array hold the spatial domain
            # co-ordinates of the associated point in some_data_grid

    # now we can use fftfreq to give us a base for the wavenumber co-ords
    # this returns [0.0 , 1.0 , 2.0 , ... , 62.0 , 63.0 , -64.0 , -63.0 , ... , -2.0 , -1.0 ]
    n_value = fftfreq( Nr , (1.0 / float(Nr) ) )
    m_value = fftfreq( Nc , (1.0 / float(Nc) ) )
    
    # now we can initialize some arrays to hold the wavenumber co-ordinates of each cell
    kx_array = zeros( SpatialArrayShape , dtype = float )
    ky_array = zeros( SpatialArrayShape , dtype = float )
    
    # before we can calculate the wavenumbers we need to know the total length of the spatial
    # domain data in x and y. This assumes that the spatial domain units are metres and
    # will result in wavenumber domain units of radians / metre.
    x_length = xsize * SourcePixelWidth
    y_length = ysize * SourcePixelHeight
    
    return Nr, Nc, x_length, y_length, kx_array, ky_array, n_value, m_value
    # To use
    # Nr, Nc, x_length, y_length, kx_array, ky_array, n_value, m_value =
    # PrepArray2Fourier (xsize, ysize, SpatialArray, ArrayOriginX, ArrayOriginY, ArrayResolutionX, ArrayResolutionY)

def Arrayfft2(SpatialArray):

    # now use the fft to transform the data to the wavenumber domain
    WaveDomainArray = fft2(SpatialArray)
    # now we can initialize some arrays to hold the wavenumber co-ordinates of each cell
    WaveDomainArray_proc = zeros( SpatialArray.shape , dtype = complex )
    
    return WaveDomainArray, WaveDomainArray_proc
    # To use
    # WaveDomainArray, WaveDomainArray_proc = Arrayfft2(SpatialArray)

def Arrayifft2(WaveDomainArray):
    SpatialArray = real(ifft2(WaveDomainArray))
    return SpatialArray
    # To use
    # SpatialArray = Arrayifft2(WaveDomainArray)

###############################################################################

FileName            =   'can1k_mag_NAD83_crop02_UTM.tiff'
TargetFileName_prol =   'can1k_mag_NAD83_crop02_UTM_prol.tiff'
TargetFileName_der1 =   'can1k_mag_NAD83_crop02_UTM_der1.tiff'
TargetFileName_RTP  =   'can1k_mag_NAD83_crop02_UTM_RTP.tiff'

#FileName       =   'CAN_Bouguer_NAD83_crop02_UTM.tiff'
#TargetFileName =   'CAN_Bouguer_NAD83_crop02_UTM_prol.tiff'

# Upward continuation
zp = -1000 # zp < 0 moves away from sources

# Champ magnetique regional
D = 0*pi/180      # declination
I = 90*pi/180     # inclination
F = 1             # intensity
# Champ magnetique regional
l = F*cos(I)*cos(D)
m = F*cos(I)*sin(D)
n = F*sin(I)

# Import data
SourceOriginX, SourceOriginY, SourcePixelWidth, SourcePixelHeight, Projection, Bands, \
SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)

# Ordre de la derivee si n positif, ou de l'integration si n negatif 
dn = 1

Nr, Nc, x_length, y_length, kx_array, ky_array, n_value, m_value =\
PrepArray2Fourier (xsize, ysize, SourceArray, SourceOriginX, SourceOriginY, \
SourcePixelWidth, SourcePixelHeight)

WaveDomainArray, WaveDomainArray_proc = Arrayfft2(SourceArray)

#WaveDomainArray_prol = WaveDomainArray_proc
#WaveDomainArray_der1 = WaveDomainArray_proc
WaveDomainArray_RTP  = WaveDomainArray_proc
# now the loops to calculate the wavenumbers
for row in xrange(Nr):
    
    for column in xrange(Nc):
        
        kx_array[row][column] = ( 2.0 * pi * n_value[column] ) / x_length
        ky_array[row][column] = ( 2.0 * pi * n_value[row] ) / y_length

# now for any row,column pair kx_array , and ky_array will hold the wavedomain coordinates
# of the correspoing point in some_data_wavedomain
        kw = sqrt(pow(kx_array[row][column],2)+pow(ky_array[row][column],2))
        
        # continuation
#        WaveDomainArray_prol [row][column] = \
#        WaveDomainArray [row][column] * exp(kw*zp)
        
        # derivative
#        WaveDomainArray_der1 [row][column] = \
#        WaveDomainArray [row][column] * \
#        (-2*pi*1j*(l*kx_array[row][column]+m*ky_array[row][column]-1j*n*kw))**dn
        
#        # Reduction au pole du vecteur champ magnetique
        A = (l*kx_array[row][column] + m*ky_array[row][column] + 1j*n*kw)

        WaveDomainArray_RTP [row][column] = \
        WaveDomainArray [row][column] * \
        1j * kw / A
        
        # Double reduction au pole (vecteurs champ magnetique et aimantation)


print WaveDomainArray_RTP


#TargetArray_prol = Arrayifft2(WaveDomainArray_prol)
#TargetArray_der1 = Arrayifft2(WaveDomainArray_der1)
TargetArray_RTP  = Arrayifft2(fftshift(WaveDomainArray_RTP))
print TargetArray_RTP
TargetType = SourceType
NDV = -99999

# Export
#CreateGeoGrid(FileName, TargetFileName_prol, xsize, ysize, TargetType, TargetArray_prol, NDV)
#CreateGeoGrid(FileName, TargetFileName_der1, xsize, ysize, TargetType, TargetArray_der1, NDV)
CreateGeoGrid(FileName, TargetFileName_RTP, xsize, ysize, TargetType, TargetArray_RTP, NDV)