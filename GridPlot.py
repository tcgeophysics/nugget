# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:39:05 2013

@author: thomascampagne

Plotting input and output arrays for comparison
"""

import matplotlib.pyplot as plt
import sys
from matplotlib import cm
from numpy import percentile



def ArrayPlot(SourceArray, TargetArray,SourceOriginX, SourceOriginY, \
SourcePixelWidth, SourcePixelHeight, SameCB):
    
    SourceArrayShape = SourceArray.shape
    TargetArrayShape = TargetArray.shape
    
    
    if SourceArrayShape!= TargetArrayShape:
        print 'Arrays of different size'
        sys.exit(1)    
    
    xsize = SourceArrayShape [1] #x length
    ysize = SourceArrayShape [0] #y length
    
    xmin = SourceOriginX
    xmax = SourceOriginX + xsize * SourcePixelWidth
    ymax = SourceOriginY + ysize * SourcePixelHeight
    ymin = SourceOriginY    
    
    
    if SameCB==True:
        SourceBandMinpc = round(percentile (SourceArray,10),-1)
        SourceBandMaxpc = round(percentile (SourceArray,90), -1)
         
        print SourceBandMinpc, SourceBandMaxpc
        
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))
        fig.suptitle('Upward continuation', fontsize=16)
        ax1.set_title('Source array')
        im1 = ax1.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal',\
        vmin=SourceBandMinpc, vmax=SourceBandMaxpc, cmap=cm.jet)
        
        ax2.set_title('Target array')
        im2 = ax2.imshow(TargetArray, extent=[xmin, xmax, ymin, ymax], aspect='equal',\
        vmin=SourceBandMinpc, vmax=SourceBandMaxpc, cmap=cm.jet)
        
        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        cb = fig.colorbar(im1, cax=cbar_ax)
        cb.set_label('nT or mGal')
        
    if SameCB==False:
        fig = plt.figure(figsize=(16,6))
        fig.suptitle('Upward continuation', fontsize=16)
        
        plt.subplot(121)
        plt.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
        #plt.axis([xmin, xmax, ymin, ymax])
        plt.title("Source array")
        cb = plt.colorbar()
        cb.set_label('nT or mGal')
        
        plt.subplot(122)
        plt.imshow(TargetArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
        plt.title("Target array")
        cb = plt.colorbar()
        cb.set_label('Processed unit')
        
    fig.show()
        


    
    
    
    