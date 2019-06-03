# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:46:12 2019

@author: KIIT
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

if __name__ == '__main__':
    ax = plt.axes(xlim=(0, 20), ylim=(-6, 6))
    x = np.arange(0, 20, 0.01)
    t=  np.arange(0, 20, 0.01)
    y= 2*np.cos(1.5*t - x)*np.sin(3*t - x)
    plt.plot(x,y)
    plt.grid(True)
    plt.show()