# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:13:50 2019

@author: KIIT
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:16:35 2019

@author: KIIT
"""
import math
import os
import random
import re
import sys
import matplotlib.pyplot as plt
import numpy as np
def transitions(n,a):
    
    Eg=1.41*1.6*(10**-19)#value of the valence band in joules
    energy=[]
    energy.append(Eg)
    h=6.6*10**(-34)#Planck's constant
    a=a*(10**-9)#Coverting the nanometres to metres
    const=h*(3*(10**8))#Planck's constant multipled by speed of light
    wave1=[]
    for i in range(1,n+1):
        m=9.1*10**(-31)
        E=((i**2)*(h**2))/(8*m*a*a)#Finding energy in joules
        
        p=(const/E)*(10**10)#Finding the wavelength in armstrong
        wave1.append(p)
        energy.append(E)
    
    #print(energy)
    #Finding wavelengths from valence band
    print("\npossible wavelengths associated with the electrons in armstrong travelling from the conduction band are ",wave1)
    wave1=[]
    for i in range(1,len(energy)):
        p=(const/(Eg+energy[i]))*(10**10)#Finding the wavelength in armstrong
        wave1.append(p)
    print("\npossible wavelengths associated with the electrons in armstrong travelling from the valence band are ",wave1)
    
    for i in range(1,len(energy)):
        wave1=[]
        for j in range(1,len(energy)):
            p=(const/(energy[i]+energy[j]+Eg))*(10**10)
            wave1.append(p)
        print("\npossible wavelengths associated with the electrons in armstrong travelling from the band number ",i,wave1)



