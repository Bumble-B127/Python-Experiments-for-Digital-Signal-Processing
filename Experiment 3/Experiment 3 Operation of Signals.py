import numpy as np
import matplotlib.pyplot as plt 
from scipy import fftpack

a=np.arange(-0.02,0.02,0.0010)
b=np.arange(-0.02,0.02,0.0010)
c=np.arange(-0.02,0.02,0.00001)

s3=np.cos(2*np.pi*60*a)*15
s4=np.cos(2*np.pi*120*b + np.pi)*20
    
plt.subplot(9,2,1)
plt.stem(a,s3)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("S3[N]")
plt.ylim(-15,15)

plt.subplot(9,2,3)
plt.stem(b,s4)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("S4[N]")
plt.ylim(-20,20)

plt.subplot(9,2,2)
ft1=fftpack.fft(s3)
plt.stem(np.abs(ft1))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("S3[jw]")

plt.subplot(9,2,4)
ft2=fftpack.fft(s4)
plt.plot(np.abs(ft2))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("S4[jw]")

plt.subplot(9,2,5)
a1=s3+s4
plt.stem(a,a1)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("S3[N]+S4[N]")

plt.subplot(9,2,6)
ft3=np.fft.fft(a1)
plt.stem(np.abs(ft3))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("S3+S4[jw]")

plt.subplot(9,2,7)
a2=s3-s4
plt.stem(a,a2)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("S3[N]-S4[N]")

plt.subplot(9,2,8)
ft4=np.fft.fft(a2)
plt.stem(np.abs(ft4))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("S3-S4[jw]")

plt.subplot(9,2,9)
a3=s3*s4
plt.stem(a,a3)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("S3[N]*S4[N]")

plt.subplot(9,2,10)
ft5=np.fft.fft(a3)
plt.stem(np.abs(ft5))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("S3*S4[jw]")

plt.subplot(9,2,17)
a4=np.flip(s4)
plt.stem(a,a4)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("-S4[N]")

plt.subplot(9,2,18)
ft6=np.fft.fft(a4)
plt.stem(np.abs(ft6))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("-S4[jw]")

b1=np.arange(-0.02,0.02,0.001)
s5=np.cos(2*np.pi*120*2*b1 + np.pi)*20
plt.subplot(9,2,15)
plt.stem(a,s5)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("scaleS4[2N]")

plt.subplot(9,2,16)
ft7=np.fft.fft(s5)
plt.stem(np.abs(ft7))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("scaleS4[jw]")

s6=10+s4
plt.subplot(9,2,11)
plt.stem(a,s6)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("AmpS4[N]")

plt.subplot(9,2,12)
ft8=np.fft.fft(s6)
plt.stem(np.abs(ft8))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("AmpS4[jw]")

s7=np.cos(2*np.pi*120*b + np.pi*1.5)*20
plt.subplot(9,2,13)
plt.stem(a,s7)
plt.xlabel("N index")
plt.ylabel("Amplitude")
plt.title("PhaseS4[N]")

plt.subplot(9,2,14)
ft9=np.fft.fft(s7)
plt.stem(np.abs(ft9))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("PhaseS4[jw]")