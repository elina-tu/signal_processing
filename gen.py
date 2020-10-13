# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:16:06 2020

@author: Elina
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

def closeCallback(event):
    '''"off" button callback to close the window'''
    plt.close()

def freqCallback(val):
    '''change frequency according to slider'''
    plotHandle.set_ydata(sine(val, t))
    plt.draw()

t = 1 #s
num = 100 #number of points
freq = 1 #Hz
t = np.linspace(0, t, num)

#function for wave
sine = lambda freq, t : np.sin(2*np.pi*freq*t)

ax = plt. axes([0.15, 0.1, 0.6, 0.8])
plotHandle, = plt.plot(t, sine(freq, t), 'k-')
plt.xlabel('t, s')
plt.ylabel('f, Hz')

#off button
bax = plt.axes([0.8, 0.2, 0.1, 0.05])
buttonHandle = widgets.Button(bax, 'Off')
buttonHandle.on_clicked(closeCallback)

#frequency slider
sax = plt.axes([0.92, 0.5, 0.03, 0.4])
freqHandle = widgets.Slider(sax, 'frequency', valmin=1, valmax=10, valinit=0.5,\
                            orientation='vertical')
freqHandle.on_changed(freqCallback)

plt.show()