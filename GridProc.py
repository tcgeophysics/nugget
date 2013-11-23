# -*- coding: utf-8 -*-
"""
TC, Nov 23, 2013
Suite of 2D filters to process 2D numpy arrays from GridIO.py
"""

import sys, numpy, GridIO

# IO functions: 
# GeoT, Projection, Bands, SourceType, NDV, xsize, ysize, SourceArray, SourceStats = GetGeoGrid(FileName)
# CreateGeoGrid(FileName, TargetFileName, xsize, ysize, TargetType, TargetArray)
# Return 0 if successful