# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:16:06 2020

@author: Elina
"""

import numpy as np
import matplotlib.pyplot as plt

t = 1 #s
num = 100 #number of points
freq = 1 #Hz
t = np.linspace(0, t, num)
sine = np.sin(2*np.pi*freq*t)

plt.plot(t, sine, 'k-')
plt.xlabel('t, s')
plt.ylabel('f, Hz')
plt.show()