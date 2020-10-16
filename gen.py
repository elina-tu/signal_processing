# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:16:06 2020

@author: Elina
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

from scipy import signal
import scipy.fft as fft

def closeCallback(event):
    '''"off" button callback to close the window'''
    plt.close('all')

def freqCallback(value):
    '''change frequency according to slider'''
    if typeHandle.value_selected == 'sine':
        plotHandle.set_ydata(sine(value, phaseHandle.val, time(t0, timeHandle.val, \
                                                               int(numHandle.val))))
    elif typeHandle.value_selected == 'sawtooth':
        plotHandle.set_ydata(signal.sawtooth(2*np.pi*value*time(t0, timeHandle.val,\
                                            int(numHandle.val)) + phaseHandle.val))
    elif typeHandle.value_selected == 'square':
        plotHandle.set_ydata(signal.square(2*np.pi*value*time(t0, timeHandle.val,\
                                            int(numHandle.val)) + phaseHandle.val))

    plotHandle.set_xdata(time(t0, timeHandle.val, int(numHandle.val)))
    fft_update()
    active_graph_update()
    ax.relim()
    ax.autoscale()
    plt.draw()

def timeCallback(value):
    '''change time interval over which function is plotted'''
    if typeHandle.value_selected == 'sine':
        plotHandle.set_ydata(sine(freqHandle.val, phaseHandle.val,time(t0, value, \
                                                                int(numHandle.val))))
    elif typeHandle.value_selected == 'sawtooth':
        plotHandle.set_ydata(signal.sawtooth(2*np.pi*freqHandle.val*time(t0, value,\
                                            int(numHandle.val)) + phaseHandle.val))
    elif typeHandle.value_selected == 'square':
        plotHandle.set_ydata(signal.square(2*np.pi*freqHandle.val*time(t0, value,\
                                            int(numHandle.val)) + phaseHandle.val))

    plotHandle.set_xdata(time(t0, value, int(numHandle.val)))
    fft_update()
    active_graph_update()
    ax.relim()
    ax.autoscale()
    plt.draw()

def phaseCallback(value):
    '''change phase of the function'''
    if typeHandle.value_selected == 'sine':
        plotHandle.set_ydata(sine(freqHandle.val, value, time(t0, timeHandle.val, \
                                                          int(numHandle.val))))
    elif typeHandle.value_selected == 'sawtooth':
        plotHandle.set_ydata(signal.sawtooth(2*np.pi*freqHandle.val*time(t0, timeHandle.val,\
                                            int(numHandle.val)) + value))
    elif typeHandle.value_selected == 'square':
        plotHandle.set_ydata(signal.square(2*np.pi*freqHandle.val*time(t0, timeHandle.val,\
                                            int(numHandle.val)) + value))
    fft_update()
    active_graph_update()
    ax.relim()
    ax.autoscale()
    plt.draw()

def numCallback(value):
    '''change number of points'''
    if typeHandle.value_selected == 'sine':
        plotHandle.set_ydata(sine(freqHandle.val, phaseHandle.val, time(t0, timeHandle.val,\
                                                                        int(value))))
    elif typeHandle.value_selected == 'sawtooth':
        plotHandle.set_ydata(signal.sawtooth(2*np.pi*freqHandle.val*time(t0, timeHandle.val,\
                                            int(value)) + phaseHandle.val))
    elif typeHandle.value_selected == 'square':
        plotHandle.set_ydata(signal.square(2*np.pi*freqHandle.val*time(t0, timeHandle.val,\
                                            int(value)) + phaseHandle.val))
    plotHandle.set_xdata(time(t0, timeHandle.val, int(value)))
    wplotHandle.set_ydata(plotHandle.get_ydata()[int(value*leftcutHandle.val):int(value+1)])
    wplotHandle.set_xdata(plotHandle.get_xdata()[int(value*leftcutHandle.val):int(value+1)])
    fft_update()
    active_graph_update()
    plt.draw()

def typeCallback(label):
    '''change signal type'''
    if label == 'sine':
        plotHandle.set_ydata(sine(freqHandle.val, phaseHandle.val, time(t0, timeHandle.val,\
                                                 int(numHandle.val))))
    elif label == 'sawtooth':
        plotHandle.set_ydata(signal.sawtooth(2*np.pi*freqHandle.val*time(t0, timeHandle.val,\
                                                int(numHandle.val)) + phaseHandle.val))
    elif label == 'square':
        plotHandle.set_ydata(signal.square(2*np.pi*freqHandle.val*time(t0, timeHandle.val,\
                                            int(numHandle.val)) + phaseHandle.val))
    fft_update()
    active_graph_update()
    plt.draw()

def leftCallback(value):
    """change left start of the time interval"""
    '''if typeHandle.value_selected == 'sine':
        wplotHandle.set_ydata(sine(freqHandle.val, phaseHandle.val, time(value* timeHandle.val,\
                                                                    timeHandle.val, int(numHandle.val))))
    elif typeHandle.value_selected == 'sawtooth':
        wplotHandle.set_ydata(signal.sawtooth(2*np.pi*freqHandle.val*time(value* timeHandle.val,\
                                                    timeHandle.val, int(numHandle.val)) + phaseHandle.val))
    elif typeHandle.value_selected == 'square':
        wplotHandle.set_ydata(signal.square(2*np.pi*freqHandle.val*time(value* timeHandle.val,\
                                                timeHandle.val, int(numHandle.val)) + phaseHandle.val))'''

    #y = plotHandle.get_ydata()
    #y = y[int(numHandle.val*value):int(numHandle.val+1)]
    wplotHandle.set_ydata(plotHandle.get_ydata()[int(numHandle.val*value):int(numHandle.val+1)])
    wplotHandle.set_xdata(plotHandle.get_xdata()[int(numHandle.val*value):int(numHandle.val+1)])
    fft_update()
    plt.draw()

def fft_update():
    """function to update fourier transform plot, when other callbacks trigered"""
    yf = fft.fft(wplotHandle.get_ydata())
    if int((1-leftcutHandle.val)*numHandle.val)%2 == 0:
        fftHandle.set_ydata(abs(yf)[1:int(numHandle.val//2)]/numHandle.val)
        fftHandle.set_xdata(np.arange(1, numHandle.val//2, 1)/timeHandle.val)
    else:
        fftHandle.set_ydata(abs(yf)[1:int((numHandle.val-1)//2 + 1)]/numHandle.val)
        fftHandle.set_xdata(np.arange(1, (numHandle.val-1)//2 + 1, 1)/timeHandle.val)

    ax1.relim()
    ax1.autoscale()

def active_graph_update():
    """update graph in the window"""
    wplotHandle.set_ydata(plotHandle.get_ydata()[int(numHandle.val*leftcutHandle.val):int(numHandle.val+1)])
    wplotHandle.set_xdata(plotHandle.get_xdata()[int(numHandle.val*leftcutHandle.val):int(numHandle.val+1)])
    fft_update()
    plt.draw()

fig = plt.figure(figsize=(10, 6))

global t0
t0 = 0 #s
t = 1 #s
num = 100 #number of points
freq = 1 #Hz
phase = 0

#time array funcion
time = lambda t0, t, num: np.linspace(t0, t, num)
#function for wave
sine = lambda freq, phase, t : np.sin(2*np.pi*freq*t + phase)

y = sine(freq, phase, time(t0, t, num))
#fourier transform
yf = fft.fft(y)

ax = plt.axes([0.1, 0.55, 0.5, 0.4])
plotHandle, = plt.plot(time(t0, t, num), y, 'b-') #base plot
wplotHandle, = plt.plot(time(t0, t, num), y, 'r-') #windowed plot
plt.xlabel('t, s')
plt.ylabel('f, Hz')

#SIGNAL GRAPH CONTROL
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

#radio buttons to select type of signal
rax = plt.axes([0.7, 0.7, 0.1, 0.2])
typeHandle = widgets.RadioButtons(rax, labels=['sine', 'sawtooth', 'square'])
typeHandle.on_clicked(typeCallback)

#left cut off control
sax4 = plt.axes([0.75, 0.2, 0.1, 0.03])
leftcutHandle = widgets.Slider(sax4, 'left', valmin=0, valmax=1, valinit=0, valstep=0.01)
leftcutHandle.on_changed(leftCallback)

#FFT GRAPH
ax1 = plt.axes([0.1, 0.05, 0.5, 0.4])
fftHandle, = plt.loglog(np.arange(1, num//2, 1)/t, abs(yf)[1:num//2]/num)



plt.show()
