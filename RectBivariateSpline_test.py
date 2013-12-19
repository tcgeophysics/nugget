# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:20:09 2013

@author: thomascampagne
"""

import numpy
from scipy import interpolate
x = numpy.array([10.0, 12.0, 14.0])
y = numpy.array([10.0, 12.0, 14.0, 16.0])
z = numpy.array([ 
   [ 1.4 ,  6.5 ,  1.5 ,  1.8 ],
   [ 8.9 ,  7.3 ,  1.1 ,  1.09],
   [ 4.5 ,  9.2 ,  1.8 ,  1.2 ]])
print 'z = ', z
# you have to set kx and ky small for this small example dataset
# 3 is more usual and is the default
# s=0 will ensure this interpolates.  s>0 will smooth the data
# you can also specify a bounding box outside the data limits
# if you want to extrapolate
#sp = interpolate.RectBivariateSpline(x, y, z, kx=2, ky=2, s=0)

sp = interpolate.RectBivariateSpline(x, y, z,bbox=[6.0,18.0, 6.0,20.0],\
 kx=2, ky=2, s=0)

xx = numpy.array([6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0])
yy = numpy.array([6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0])
z_ext = sp (xx, yy)

print 'z extra = ', z_ext

sp([0.60], [0.25])  # array([[ 7.3]])
sp([0.25], [0.60])  # array([[ 2.66427408]])