# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:45:32 2019

@author: MAYUKH MALLICK 1806391 at KIIT DEEMED UNIVERSITY,BBSR,ODISHA,INDIA
"""

import math
import os
import random
import re
import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab
from IPython import get_ipython

arr3=[]
def energy(n,sample):
    h=6.6*10**(-34)
    m=9.1*10**(-31)
    E=((n**2)*(h**2))/(8*m*sample*sample)
    #print(E)
    E=E/(1.6*10**(-19))
    print("\nEnergy of the particle in the given principle quantum number in eV ",E)
    
def probabilityPlot(n,sample):
    step=1
    if(sample<1):
        step=0.00001
    elif(sample>=1 and sample<100):
        step=0.01
    #elif(sample>=10 and sample<=100):
        #step=0.1
    else:
        step=1
    x = np.arange(0,sample,step)
    a=(n*np.pi *x /sample)
    y =((np.sin(a)**2)*((2/sample)))
    
    plt.plot(x, y,color='red')
    #plt.scatter(x, y,colour='black')
    plt.title("Probability particle density graph")
    plt.xlabel('a in nanometers')
    plt.ylabel('V(x)')
    plt.grid(True)
    
    plt.show()
    print("maximum value of the probability wave function",max(y))
    

def wavePlot(n,sample):
    step=1
    if(sample<1):
        step=0.00001
    elif(sample>=1 and sample<80):
    
        step=0.01
    #elif(sample>=10 and sample<=100):
        #step=0.1
    else:
        step=1
    
    x = np.arange(0,sample,step)
    a=(n*np.pi *x /sample)
    y = (np.sin(a))*((2/sample)**0.5)
    plt.plot(x, y,color='blue')
    plt.title('Wave function graph')
    plt.xlabel('a in nanometers')
    plt.ylabel('V(x)')
    plt.grid(True)
    plt.show()
    print("maximum value of the wave function",max(y))
    
    
def plots(n,sample):
    step=1
    if(sample<1):
        step=0.00001
    elif(sample>=1 and sample<100):
        step=0.01
    #elif(sample>=10 and sample<=100):
        #step=0.1
    else:
        step=1
    
    x = np.arange(0,sample,step)
    a=(n*np.pi *x /sample)
    y = (np.sin(a))*((2/sample)**0.5)
    y1=((np.sin(a)**2)*((2/sample)))
    plt.plot(x,y,'-b',label='wave function')
    plt.plot(x,y1,'-r',label='probability graph')
    plt.legend(loc='lower left')
    plt.xlabel('a in nanometers')
    plt.ylabel('V(x)')
    plt.grid(True)
    
    plt.show()
    arr1=list(y)
    arr2=list(y1)
    arr3=list(x)
    arrwave=[]
    arrprob=[]
    m1=max(arr1)
    m2=min(arr1)
    
    for i in range(0,len(arr1)):
        if(arr1[i]==m1):
            arrwave.append(arr3[i])
            arrprob.append(arr3[i])
        if(arr1[i]==m2):
            arrprob.append(arr3[i])
    
    print("Maximum values of wave function is/are found to be at",arrwave)
    if(n==1):
        print("Point(s) where probability of finding electrons are maximum at",arrwave)
    else:
        print("Point(s) where probability of finding electrons are maximum at",arrprob)

    

    