# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:20:33 2013

@author: thomascampagne
"""

# Programme de modelisation magnetisme 

# Modelisation de deux sources parallepipede identiques a diff屍entes
# profondeurs
# Prolongement et comparaisons
# Campagne Thomas EOST 3A Novembre 2007
import numpy as np
from numpy.fft import *
from cmath import exp
from math import pi, cos, sin, sqrt
import matplotlib.pyplot as plt
import matplotlib.cm as cm

D = 10*pi/180     # declinaison du champ magnetique regional
I = 64*pi/180    # inclinaison du champ magnetique regional
F = 1             # intensite du champ magnetique regional

D0 = 10*pi/180    # declinaison de l'aimantation
I0 = 80*pi/180    # inclinaison de l'aimantation
m0 = 1           # aimantation 

# champ magnetique regional
l = F*cos(I)*cos(D)
m = F*cos(I)*sin(D)
n = F*sin(I)
# vecteur aimantation
L = cos(I0)*cos(D0)
M = cos(I0)*sin(D0)
N = sin(I0)
# domaine spatial reel
x = range(1,100)
y = range(1,100)

# localisation du corp 
x1 = 45.0
x2 = 55.0
y1 = 45.0
y2 = 55.0
z1 = 10.0
z2 = 15.0

# Altitude du prolongement, zp > 0 vers la structure, 
#  zp < 0 dans la direction opposee
zp1 = 10.0
zp2 = 5.0
zp3 = -5.0

# Profil extrait
xprof = 50.0

ftild = np.zeros((len(x),len(y)), dtype=complex) # creation de la matrice de zeros ftild
ftild1_p = ftild
ftild2_p = ftild
ftild3_p = ftild

for f in range(1,len(x)):
    
    u = ((f-1)/float(len(x)))*2*pi      # passage au domaine spectral  
    
    if u>=pi : u=u-2*pi        # condition sur [0;pi]U[-pi;0[
    
    for g in range(1,len(y)):
        v = ((g-1)/float(len(y)))*2*pi   # passage au domaine spectral   
        
        if v>=pi : v=v-2*pi      # condition sur [0;pi]U[-pi;0[
        if u==0 : ExpX=1j*(x1-x2)
        else : ExpX=((exp(1j*u*x1) - exp(1j*u*x2))/u)
        if v==0 : ExpY=1j*(y1-y2)
        else : ExpY=((exp(1j*v*y1) - exp(1j*v*y2))/v)
        if u==0 and v==0 : ftild [f][g]=0
        else :
            w=sqrt(u*u + v*v)
            #print 'ExpX ', ExpX,'\nExpY ',ExpY
            a = ((2*pi*m0)/w) * ExpX * ExpY
            b = ((exp(-w*z1) - exp(-w*z2))/(w))
            c = (l*u + m*v - 1j*n*w)
            d = (L*u + M*v - 1j*N*w)
            ftild [f][g] = a * b * c * d
#            ftild [f][g] = ((2*pi*m0)/w) * ExpX * ExpY *\
#                    ((exp(-w*z1) - exp(-w*z2))/(w))*\
#                    (l*u + m*v - 1j*n*w)*\
#                    (L*u + M*v - 1j*N*w)
            
# Prolongements
            ftild1_p [f][g] = ftild [f][g] * exp(w*zp1)
            ftild2_p [f][g] = ftild [f][g] * exp(w*zp2)
            ftild3_p [f][g] = ftild [f][g] * exp(w*zp3)
            

# TF2D inverse 
#Ys= fftshift(ftild)
#Y=ifft2(Ys)
#Yr = np.real(Y)
Yr = np.real(ifft2(fftshift(ftild)))
Yp1=ifft2(ftild1_p)
Ypr1 = np.real(Yp1)
Yp2=ifft2(ftild2_p)
Ypr2 = np.real(Yp2)
Yp3=ifft2(ftild3_p)
Ypr3 = np.real(Yp3)

zp1s = str(zp1)
zp2s = str(zp2)
zp3s = str(zp3)
z1s = str(z1)


plt.title('Anomalie Magnetique')

plt.subplot(2,2,1)
plt.imshow(Yr, cmap=cm.rainbow, interpolation='nearest')

plt.subplot(2,2,2)
plt.imshow(Ypr1, cmap=cm.rainbow, interpolation='nearest')

plt.subplot(2,2,3)
plt.imshow(Ypr2, cmap=cm.rainbow, interpolation='nearest')

plt.subplot(2,2,4)
plt.imshow(Ypr3, cmap=cm.rainbow, interpolation='nearest')

plt.show()

#
#
#         # interpolation/ lissage de la carte
## xlabel('Distance en m')
## ylabel('Distance en m')
#hold on
#plot (ones(1,length(x))*(xprof+1),y,'k')
#title('Anomalie Magnetique'); colorbar
#patch([x1+1,x2+1,x2+1,x1+1,x1+1],[y2+1,y2+1,y1+1,y1+1,y2+1],'k','FaceColor','None') # plot du modele
#
#subplot 222
#pcolor(x,y,Ypr1); shading interp              # interpolation/ lissage de la carte
## xlabel('Distance en m')
## ylabel('Distance en m')
#hold on
#plot (ones(1,length(x))*(xprof+1),y,'k')
#title(['Prolongement de ',zp1s]); colorbar
#patch([x1+1,x2+1,x2+1,x1+1,x1+1],[y2+1,y2+1,y1+1,y1+1,y2+1],'k','FaceColor','None') # plot du modele
#
#subplot 223
#pcolor(x,y,Ypr2); shading interp              # interpolation/ lissage de la carte
## xlabel('Distance en m')
## ylabel('Distance en m')
#hold on
#plot (ones(1,length(x))*(xprof+1),y,'k')
#title(['Prolongement de ',zp2s]); colorbar
#patch([x1+1,x2+1,x2+1,x1+1,x1+1],[y2+1,y2+1,y1+1,y1+1,y2+1],'k','FaceColor','None') # plot du modele
#
#subplot 224
#pcolor(x,y,Ypr2); shading interp              # interpolation/ lissage de la carte
## xlabel('Distance en m')
## ylabel('Distance en m')
#hold on
#plot (ones(1,length(x))*(xprof+1),y,'k')
#title(['Prolongement de ',zp3s]); colorbar
#patch([x1+1,x2+1,x2+1,x1+1,x1+1],[y2+1,y2+1,y1+1,y1+1,y2+1],'k','FaceColor','None') # plot du modele
#
#figure('Name','Profils extraits')
#xprofs=num2str(xprof);
## A1 = max(Yr1(:,xprof))
## A2 = max(Yr2(:,xprof))
## P1 = max(Ypr1(:,xprof))
## P2 = max(Ypr2(:,xprof))
#plot(x,Yr(:,xprof),x,Ypr1(:,xprof),x,Ypr2(:,xprof),x,Ypr3(:,xprof))
#title(['Profil a y = ',xprofs,'m extrait des differentes cartes'])
##legend('Anomalie Magnetique 1','Anomalie Magnetique 2',...
##    'Prolongement de zp1s','Prolongement de zp2s')
#legend(['Anomalie Magnetique 1 a z= ',z1s,'m'],...
#    ['Prolongement de ',zp1s],['Prolongement de ',zp2s],...
#    ['Prolongement de ',zp3s])


