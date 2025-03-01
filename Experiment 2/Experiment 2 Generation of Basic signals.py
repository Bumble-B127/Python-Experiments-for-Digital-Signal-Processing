# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:54:30 2024

@author: cb.en.u4ece22151
"""

import numpy as np
import matplotlib.pyplot as plt

def unit_step(t):
    return np.heaviside(t,1)

def unit_impulse(t):
    return np.where(t==0,1,0)

def ramp(t):
    return np.where(t>=0,t,0)

def exp_decay(t):
    return np.exp(-t)

def exp_rising(t):
    return np.exp(t)


c=np.linspace(-5, 5,100)
d=np.linspace(-5, 5,20)

plt.subplot(8,2,1)
a=unit_step(c)
plt.plot(c,a)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Continuous unit step")

plt.subplot(8,2,2)
b=unit_step(d)
plt.stem(d,b)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("Discrete unit step")

plt.subplot(8,2,3)
q=unit_impulse(c)
plt.plot(c,q)
plt.stem([0],[1],"--")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Continuous Unit impulse")

plt.subplot(8,2,4)
w=unit_impulse(d)
plt.stem(d,w)
plt.stem([0],[1])
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("Discrete Unit impulse")

plt.subplot(8,2,5)
r=ramp(c)
plt.plot(c,r)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Continuous Ramp")

plt.subplot(8,2,6)
t=ramp(d)
plt.stem(d,t)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("Discrete Ramp")

plt.subplot(8,2,7)
y=exp_decay(c)
plt.plot(c,y)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Continuous Exponential Decay")

plt.subplot(8,2,8)
u=exp_decay(d)
plt.stem(d,u)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("Discrete Exponential Decay")

plt.subplot(8,2,9)
i=exp_rising(c)
plt.plot(c,i)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Continuous Exponential Rising")

plt.subplot(8,2,10)
o=exp_rising(d)
plt.stem(d,o)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("Discrete Exponential Decay")


c1=np.linspace(-3, 3,100)
z=np.arange(np.pi,5*np.pi,0.5)

plt.subplot(8,2,11)
l=np.sin(z)*2
plt.plot(z/(60*np.pi),l)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Continuous Sinusoidal")

plt.subplot(8,2,12)
k=np.sin(z)*2
plt.stem(z/(60*np.pi),k)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("Discrete Sinusoidal")


