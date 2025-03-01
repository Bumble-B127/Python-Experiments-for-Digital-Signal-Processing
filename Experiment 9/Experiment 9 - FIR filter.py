# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:19:04 2024

@author: sanja
"""

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.signal import freqz

wc=(np.pi/3)
M=11
a=(M-1)/2
b=(wc/np.pi)

hd_n=[]

n = np.arange(M)
hd_n = np.sin(wc * (n - a)) / (np.pi * (n - a))
hd_n[M // 2] = b

def rectangular_window(M):
    n = np.arange(M)
    n[0]=1
    return n/n

def hamming_window(M):
    n = np.arange(M)
    return 0.54 - 0.46 * np.cos(2 * np.pi * n / (M - 1))    

def hanning_window(M):
    n = np.arange(M)
    return 0.5 - 0.5 * np.cos(2 * np.pi * n / (M - 1))


hn_r= hd_n * rectangular_window(M)
print("Rectangular window coefficients:",hn_r)

plt.figure(2)
plt.subplot(3,1,1)
wr,Hr=freqz(hn_r)
plt.plot(wr*57.29, 20*np.log10(abs(Hr)))
plt.grid(True)
plt.title('Frequency Response of Linear Phase Low-pass FIR Filter - Rectangular window')
plt.xlabel('Frequency (degrees)')
plt.ylabel('Magnitude (dB)')


hn_m = hd_n * hamming_window(M)
print("\n Hamming window coefficients:",hn_m)

wm,Hm=freqz(hn_m)
plt.subplot(3,1,2)
plt.grid(True)
plt.plot(wm*57.29,20 * np.log10(abs(Hm)))
plt.title('Frequency Response of Linear Phase Low-pass FIR Filter - Hamming window')
plt.xlabel('Frequency (degrees)')
plt.ylabel('Magnitude (dB)')

hn_n = hd_n * hanning_window(M)
print("\n Hanning window coefficients:",hn_n)

wn,Hn=freqz(hn_n)
plt.subplot(3,1,3)
plt.grid(True)
plt.plot(wn*57.29,20 * np.log10(abs(Hn)))
plt.title('Frequency Response of Linear Phase Low-pass FIR Filter - Hanning window')
plt.xlabel('Frequency (degrees)')
plt.ylabel('Magnitude (dB)')

plt.figure(1)

plt.subplot(311)
plt.stem(hn_r)
plt.title('window Coefficients - Rectangular window')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.subplot(312)
plt.stem(hn_m)
plt.title('window Coefficients - Hamming window')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.subplot(313)
plt.stem(hn_n)
plt.title('window Coefficients - Hanning window')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.figure(3)

plt.subplot(3,1,1)
plt.grid(True)
plt.plot(wr*57.29,np.angle(Hr))
plt.title('Phase Response of Low-pass FIR Filter - Rectangular window')
plt.xlabel('Frequency (degrees)')
plt.ylabel('Phase')

plt.subplot(3,1,2)
plt.grid(True)
plt.plot(wm*57.29,np.angle(Hm))
plt.title('Phase Response of Low-pass FIR Filter - Hamming window')
plt.xlabel('Frequency (degrees)')
plt.ylabel('Phase')

plt.subplot(3,1,3)
plt.grid(True)
plt.plot(wn*57.29,np.angle(Hn))
plt.title('Phase Response of Low-pass FIR Filter - Hanning window')
plt.xlabel('Frequency (degrees)')
plt.ylabel('Phase')



















