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
    
    # Check if arrays are of same size
    if SourceArrayShape!= TargetArrayShape:
        print 'Arrays of different size'
        sys.exit(1)    
    
    xsize = SourceArrayShape [1] #x length
    ysize = SourceArrayShape [0] #y length
    
    # Calculate array extents
    xmin = SourceOriginX
    xmax = SourceOriginX + xsize * SourcePixelWidth
    ymax = SourceOriginY + ysize * SourcePixelHeight
    ymin = SourceOriginY
    
    # Calculate 10th and 90th percentile
    SourceBandMinpc = round(percentile (SourceArray,10),-1)
    SourceBandMaxpc = round(percentile (SourceArray,90), -1)
    
    # Creating figure and subplots
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))
    
    # Same Color Bar for both plots if True, separate if False
    if SameCB==True:
#        SourceBandMinpc = round(percentile (SourceArray,10),-1)
#        SourceBandMaxpc = round(percentile (SourceArray,90), -1)
         
        
#        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))
        fig.suptitle('Upward continuation', fontsize=16)
        ax1.set_title('Source array')
        # Plot array with calculated extents and colorbar bounds
        im1 = ax1.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal',\
        vmin=SourceBandMinpc, vmax=SourceBandMaxpc, cmap=cm.jet)
        # Remove plot border to see edge effects
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_visible(False)
        ax1.spines['bottom'].set_visible(False)
        

        ax2.set_title('Target array')
        im2 = ax2.imshow(TargetArray, extent=[xmin, xmax, ymin, ymax], aspect='equal',\
        vmin=SourceBandMinpc, vmax=SourceBandMaxpc, cmap=cm.jet)
        ax2.spines['right'].set_visible(False)
        ax2.spines['top'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)
        
        # Set lateral colorbar
        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        cb = fig.colorbar(im1, cax=cbar_ax)
        cb.set_label('nT or mGal')
        
    if SameCB==False:
        # Calculate 10th and 90th percentile
        TargetBandMinpc = percentile (TargetArray,10)
        TargetBandMaxpc = percentile (TargetArray,90)
#        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16,6))

        ax1.set_title('Source array')
        im1 = ax1.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal',\
        vmin=SourceBandMinpc, vmax=SourceBandMaxpc, cmap=cm.jet)
        fig.colorbar(im1, ax=ax1, shrink=0.9)
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_visible(False)
        ax1.spines['bottom'].set_visible(False)
        
        ax2.set_title('Target array')
        im2 = ax2.imshow(TargetArray, extent=[xmin, xmax, ymin, ymax], aspect='equal',\
        vmin=TargetBandMinpc, vmax=TargetBandMaxpc, cmap=cm.jet)
        fig.colorbar(im2, ax=ax2, shrink=0.9)
        ax2.spines['right'].set_visible(False)
        ax2.spines['top'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)
        
#        fig = plt.figure(figsize=(16,6))
#        fig.suptitle('Upward continuation', fontsize=16)
#        
#        plt.subplot(121)
#        plt.imshow(SourceArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
#        #plt.axis([xmin, xmax, ymin, ymax])
#        plt.title("Source array")
#        cb = plt.colorbar()
#        cb.set_label('nT or mGal')
#        
#        plt.subplot(122)
#        plt.imshow(TargetArray, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap=cm.jet)
#        plt.title("Target array")
#        cb = plt.colorbar()
#        cb.set_label('Processed unit')
    

    fig.show()
        


    
    
    
    