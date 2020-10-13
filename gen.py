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

def freqCallback(value):
    '''change frequency according to slider'''
    plotHandle.set_ydata(sine(value, phaseHandle.val, time(timeHandle.val, \
                                                           int(numHandle.val))))
    plotHandle.set_xdata(time(timeHandle.val, int(numHandle.val)))
    ax.relim()
    ax.autoscale_view()
    plt.draw()

def timeCallback(value):
    '''change time interval over which function is plotted'''
    plotHandle.set_ydata(sine(freqHandle.val, phaseHandle.val,time(value, \
                                                            int(numHandle.val))))
    plotHandle.set_xdata(time(value, int(numHandle.val)))
    ax.relim()
    ax.autoscale_view()
    plt.draw()

def phaseCallback(value):
    '''change phase of the function'''
    plotHandle.set_ydata(sine(freqHandle.val, value, time(timeHandle.val, \
                                                          int(numHandle.val))))
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    
def numCallback(value):
    '''change number of points'''
    plotHandle.set_ydata(sine(freqHandle.val, phaseHandle.val, time(timeHandle.val,\
                                                                    int(value))))
    plotHandle.set_xdata(time(timeHandle.val, int(value)))
    plt.draw()
    
fig = plt.figure(figsize=(10, 6))

t = 1 #s
num = 100 #number of points
freq = 1 #Hz
phase = 0

#time array funcion
time = lambda t, num: np.linspace(0, t, num)
#function for wave
sine = lambda freq, phase, t : np.sin(2*np.pi*freq*t + phase)

ax = plt.axes([0.1, 0.1, 0.5, 0.8])
plotHandle, = plt.plot(time(t, num), sine(freq, phase, time(t, num)), 'k-')
plt.xlabel('t, s')
plt.ylabel('f, Hz')

#off button
bax = plt.axes([0.75, 0.1, 0.1, 0.05])
buttonHandle = widgets.Button(bax, 'Off')
buttonHandle.on_clicked(closeCallback)

#frequency slider
sax = plt.axes([0.92, 0.5, 0.02, 0.4])
freqHandle = widgets.Slider(sax, 'frequency', valmin=1, valmax=10, valinit=1,\
                            orientation='vertical')
freqHandle.on_changed(freqCallback)

#time slider
sax1 = plt.axes([0.75, 0.5, 0.1, 0.03])
timeHandle = widgets.Slider(sax1, 'time interval', valmin=0.1, valmax=10, valinit=t)
timeHandle.on_changed(timeCallback)

#phase slider
sax2 = plt.axes([0.75, 0.4, 0.1, 0.03])
phaseHandle = widgets.Slider(sax2, 'phase', valmin=0, valmax=2*np.pi, valinit=phase)
phaseHandle.on_changed(phaseCallback)

#number of points slider
sax3 = plt.axes([0.75, 0.3, 0.1, 0.03])
numHandle = widgets.Slider(sax3, 'sample number', valmin=2, valmax=500, valinit=num, \
                           valfmt='%d', valstep=1)
numHandle.on_changed(numCallback)

plt.show()