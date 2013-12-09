#!/usr/bin/env python

from distutils.core import setup, Extension
import numpy.distutils.misc_util

 
bilinearinterp_module = Extension('bilinearinterp',
                                  sources = ['bilinearinterp.c'],
#                                  define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
                                  include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs(),
#                                  include_dirs =  ['/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/core/include'],
    )

           
 
setup (name = 'bilinearinterp',
       version = '1.1',
       author      = "Space Telescope Science Institute - stsci_python",
       description = """bilinear interpolation for 2D array extrapolation""",
       ext_modules = [bilinearinterp_module],
       py_modules = ["bilinearinterp"],
       )
