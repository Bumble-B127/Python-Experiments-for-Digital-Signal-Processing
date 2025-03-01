# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:48:21 2024

@author: cb.en.u4ece22151
"""

import numpy as np
import matplotlib.pyplot as plt

plt.subplot(4,4,1)
t1=np.arange(-3,3)
x=[-3,-2,-1,1,2,3]
plt.stem(x)
plt.title("x[n]")
plt.ylabel("Amplitude")
plt.xlabel("n")

plt.subplot(4,4,2)
t=np.arange(0,4)
h=[1,-1,1,-1]
plt.stem(t,h)
plt.title("h[n]")
plt.ylabel("Amplitude")
plt.xlabel("n")


def conv(x,h):
    N=len(x)
    M=len(h)
    y=np.zeros(N+M-1)
    for n in range(N+M-1):
        for k in range(max(0,n-M+1),min(n+1,N)):
            y[n]+=x[k]*h[n-k]
        plt.subplot(4,4,n+3)
        plt.title("Intermediate plot")
        plt.ylabel("Amplitude")
        plt.xlabel("n")
        plt.stem(t,y)
        if n==8:
            plt.subplot(4,4,11)
            plt.title("Final output")

t=np.arange(-3,6)
conv(x,h)

plt.subplot(4,4,12)
con=np.convolve(x,h)
plt.title("Module output")
plt.ylabel("Amplitude")
plt.xlabel("n")
plt.stem(t,con)
plt.tight_layout(pad=0.2)


    
