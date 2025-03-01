import numpy as np ,matplotlib.pyplot as plt
from scipy.fft import fft,ifft 

fs=450

tstep=1/fs
fo=30

N=int(fs/fo)

t=np.linspace(0,(N-1)*tstep,N)

fstep=fs/N

f=np.linspace(0,(N-1)*fstep,N)

x=20*np.cos(2*np.pi*fo*t + (np.pi))

plt.figure(1)                       ##generating the input sinusoid
plt.stem(t,x)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("S2[n]")
plt.suptitle("Input Signal\n\nAmplitude = 10   Frequency = 15Hz   Phase Shift = 180 degrees")

plt.figure(2)                       ##computing user defined dft 
plt.suptitle("Forward DFT")
c=[sum(x[n]*np.exp(-2j*np.pi*k*n/N)for n in range(N)) for k in range(N)]

plt.subplot(221)                    #plotting the magnitude spectrum
plt.stem(f,np.abs(c))
plt.xlabel("k")
plt.ylabel("Amplitude")
plt.title("DFT from User's Program (Magnitude)")

plt.subplot(222)                    #plotting the phase spectrum
plt.plot(np.angle(c))
plt.xlabel("k")
plt.ylabel("Angle")
plt.title("DFT from User's Program (Angle)")

c1=fft(x)                           #computing dft in user defined function
plt.subplot(223)                    #plotting the magnitude spectrum
plt.stem(f,np.abs(c1))
plt.xlabel("k")
plt.ylabel("Amplitude")
plt.title("DFT from Built-in Function (Magnitude)")

plt.subplot(224)                    #plotting the phase spectrum
plt.plot(np.angle(c1))
plt.xlabel("k")
plt.ylabel("Angle")
plt.title("DFT from Built-in Function (Angle)")

plt.figure(3)                       ##computing user defined inverse dft
y=[sum(c[k]*np.exp(2j*np.pi*k*n/N)for k in range(N))/N for n in range(N)]

plt.subplot(221)                    #plotting the magnitude spectrum
plt.stem(t,np.real(y))
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("IDFT from User's Program (Magnitude)")

plt.subplot(222)                    #plotting the phase spectrum
plt.plot(np.angle(y))
plt.xlabel("k")
plt.ylabel("Angle")
plt.title("IDFT from User's Program (Angle)")
print(y)                            #printing the complex list comtaining the signal

y1=ifft(c)                          #computing inverse dft in user defined function
plt.subplot(223)                    #plotting the magnitude spectrum
plt.stem(t,np.real(y1))
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("IDFT from Built-in Function (Magnitude)")
print(y1)

plt.subplot(224)                    #plotting the phase spectrum
plt.plot(np.angle(y1))
plt.xlabel("k")
plt.ylabel("Angle")
plt.title("IDFT from Built-in Function (Angle)")

