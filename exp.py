import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

from audio2numpy import open_audio
import matplotlib.widgets as widgets
import sounddevice as sd

#x = np.linspace(0, 2, 200)
#freq = 3
#y = np.sin(2*np.pi*freq*x)


def originalCallback(event):
    '''Play ofiginal audio signal'''
    sd.play(y, sample_rate)

def filteredCallback(event):
    #global ift_y
    sd.play(ift_y.real, sample_rate)

y, sample_rate = open_audio('Forest.wav')
#audio sample from https://www.projectrhea.org/rhea/index.php/Audio_Signal_Filtering
y_len = len(y)
#time array
x = np.arange(0, y_len, 1)/sample_rate

#fourier fransform
yf = fft.fft(y)
yfplot = abs(yf)

#frequency cut off
filter = 1000

#figure
plt.figure(figsize=(10, 6))
#plot of original signal
ax = plt.axes([0.05, 0.48, 0.45, 0.45])
originalPlot, = plt.plot(x, y, '--g', lw=1)

#original signal fourier
y_constr = fft.ifft(yf)
#max abs frequency
max_freq = ((y_len-1)//2)/(y_len/sample_rate)
#setting powers for frequencies higher than filter to 0
y_new = np.copy(yf)
y_new[int(filter/(2*max_freq)*y_len + 1):int((1 - filter/(2*max_freq))*y_len + 1)] = 0
#reconstruction of filtered signal
ift_y = fft.ifft(y_new)
freq_pow = abs(y_new)

#filtered signal
ax1 = plt.axes([0.05, 0.02, 0.45, 0.45])
resultPlot,  = plt.plot(x, ift_y.real, '-r', lw=1)

#plot of frequency power
ax2 = plt.axes([0.55, 0.7, 0.4, 0.2])
plt.plot(np.arange(1, y_len//2, 1)/(y_len/sample_rate), yfplot[1:y_len//2]/y_len)

#plot of filtered frequencies
ax3 = plt.axes([0.55, 0.4, 0.4, 0.2])
plt.plot(np.arange(1, y_len//2, 1)/(y_len/sample_rate), freq_pow[1:y_len//2]/y_len)


#orininal button
bax = plt.axes([0.7, 0.1, 0.1, 0.05])
buttonHandle = widgets.Button(bax, 'original')
buttonHandle.on_clicked(originalCallback)

#filtered button
bax1 = plt.axes([0.7, 0.17, 0.1, 0.05])
buttonHandle1 = widgets.Button(bax1, 'filtered')
buttonHandle1.on_clicked(filteredCallback)

#text field for filter value
plt.show()
