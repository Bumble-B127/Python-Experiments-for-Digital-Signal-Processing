# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:50:39 2024

@author: CB.EN.U4ECE22151
"""

import numpy as np ,matplotlib.pyplot as plt
from scipy.fft import fft

plt.figure(1)
plt.suptitle("Input and Impulse signal")
t3=np.arange(-1,2)
h1=[2,-4,2]
t4=np.arange(0,6)
x1=[3,-6,9,-12,15,-18]

g=len(x1)
h=len(h1)
if g!=h:
    count=g+h-1
    x1=np.pad(x1,(0,count-g))
    h1=np.pad(h1,(0,count-h))

plt.subplot(1,2,2)
plt.title("h[n]")
plt.xlabel("n")
plt.ylabel("Ampitude")
t1=np.arange(-1,7)
plt.stem(t1,h1)

plt.subplot(1,2,1)
plt.title("x[n]")
plt.xlabel("n")
plt.ylabel("Ampitude")
t2=np.arange(0,8)
plt.stem(t2,x1)


def circ_conv(x1,x2):
    N=len(x1)
    y=np.zeros_like(x1,complex)
    for i in range(N):
        for k in range(N):
            if(i-k)>=0:
                y[i]+=x1[k]*x2[i-k]
            else:
                y[i]+=x1[k]*x2[N-k+i]
        
    return y.real

s=circ_conv(x1,h1)
plt.figure(2)
plt.subplot(1,2,1)
plt.title("y[n] with circular convolution function")
plt.xlabel("n")
plt.ylabel("Ampitude")
plt.stem(np.arange(-1,7),s)

s2=np.convolve(x1,h1)
plt.subplot(1,2,2)
plt.title("y[n] with built in convolution function")
plt.xlabel("n")
plt.ylabel("Ampitude")
plt.stem(np.arange(-1,14),s2)

def dft(x):
    N1=len(x)
    c=[sum(x[n]*np.exp(-2j*np.pi*k*n/N1)for n in range(N1)) for k in range(N1)]
    return np.array(c)

def idft(x):
    N1=len(x)
    c2=[sum(x[k]*np.exp(2j*np.pi*k*n/N1)for k in range(N1))/N1 for n in range(N1)]    
    return np.array(c2)

plt.figure(3)
a=dft(x1)
plt.subplot(2,2,1)
plt.title("DFT of x[n] with loop function")
plt.xlabel("k")
plt.ylabel("Ampitude")
plt.stem(a)

b=dft(h1)
plt.subplot(2,2,2)
plt.title("DFT of h[n] with loop function")
plt.xlabel("k")
plt.ylabel("Ampitude")
plt.stem(b)

a1=fft(x1)
plt.subplot(2,2,3)
plt.title("DFT of x[n] with built in function")
plt.xlabel("k")
plt.ylabel("Ampitude")
plt.stem(a1)

b1=fft(h1)
plt.subplot(2,2,4)
plt.title("DFT of h[n] with built in function")
plt.xlabel("k")
plt.ylabel("Ampitude")
plt.stem(b1)

plt.figure(4)
c=a*b
plt.subplot(1,2,1)
plt.title("X[k]*H[k]")
plt.xlabel("k")
plt.ylabel("Ampitude")
plt.stem(c)

d=idft(c)
plt.subplot(1,2,2)
plt.title("IDFT of X[k]*H[k]")
plt.xlabel("n")
plt.ylabel("Ampitude")
plt.stem(np.arange(-1,7),d)

plt.figure(5)
plt.subplot(1,3,1)
plt.title("y[n] with circular convolution function")
plt.xlabel("n")
plt.ylabel("Ampitude")
plt.stem(np.arange(-1,7),s)

plt.subplot(1,3,2)
plt.title("y[n] with built in convolution function")
plt.xlabel("n")
plt.ylabel("Ampitude")
plt.stem(np.arange(-1,14),s2)

plt.subplot(1,3,3)
plt.title("IDFT of X[k]*H[k]")
plt.xlabel("n")
plt.ylabel("Ampitude")
plt.stem(np.arange(-1,7),d)


