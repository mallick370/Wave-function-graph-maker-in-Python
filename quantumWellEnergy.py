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

def energy(n,sample):
    h=6.6*10**(-34)
    m=9.1*10**(-31)
    E=((n**2)*math.pi*math.pi*(h**2))/(2*m*sample*sample)
    E=E/(1.6*10**(-19))
    print("\nEnergy of the particle in the given principle quantum number in eV ",E)
    
def probabilityPlot(n,sample):
    step=1
    if(sample<100):
        step=0.0001
    else:
        step=1
    x = np.arange(0,sample,step)
    a=(n*np.pi *x /sample)
    y =((np.sin(a)**2)*((2/sample)))
    plt.plot(x, y,color='red')
    plt.title("Probability particle density graph")
    plt.xlabel('a in nanometers')
    plt.ylabel('V(x)')
    plt.show()
    

def wavePlot(n,sample):
    step=1
    if(sample<100):
        step=0.0001
    else:
        step=1
    
    x = np.arange(0,sample,step)
    a=(n*np.pi *x /sample)
    y = (np.sin(a))*((2/sample)**0.5)
    plt.plot(x, y,color='blue')
    plt.title('Wave function graph')
    plt.xlabel('a in nanometers')
    plt.ylabel('V(x)')
    
    plt.show()
    
    
    
if __name__ == '__main__':
    n=int(input("Enter the value of principle quantum number\n"))
    
    a=float(input("Enter the length of the quantum box or of the well in nanometers\n"))
    
    wavePlot(n,a)
    probabilityPlot(n,a)
    k=a/(10**(-9))#converting nanometer to meters
    energy(n,k)
    
    