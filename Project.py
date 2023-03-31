# -*- coding: utf-8 -*-
"""
Created on Sat May  7 22:16:58 2022

@author: mohamed
"""
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
𝑡=np.linspace(0,3,12*1024)
x=0
p=np.pi
F=[130.81,146.83,164.81,174.61,196,220,246.93]
f=[261.63,293.66,329.63,349.23,392,440,493.88]
for i in range(0,7):
   x1=np.where(t>=(i/3),1,0)
   x2=np.where(t>=((i/3)+(i/19)),1,0)
   x=x+((np.sin(2*p*F[i]*t)+np.sin(2*p*f[i]*t))*(x1-x2))
plt.subplot(3, 2,1)
plt.plot(t,x)
n=3*1024
f=np.linspace(0,512,int(n/2))
xf = fft(x)
xf = 2/n * np.abs(xf[0:int(n/2)])
plt.subplot(3, 2,2)
plt.plot(f,xf)
f1 = np.random.randint(0,512,2)
noise = np.sin(2*f1[0]*p*t)+np.sin(2*f1[1]*p*t)
dawsha = x+noise
plt.subplot(3, 2,3)
plt.plot(t,dawsha)
xf = fft(dawsha)
xf = 2/n * np.abs(xf[0:int(n/2)])
plt.subplot(3, 2,4)
plt.plot(f,xf)
s = xf.size
tmp1 = -1
ind1 = 0
for i in range(0,s):
    if(xf[i]>tmp1):
      tmp1 = xf[i]
      ind1 = i
tmp2 = -1
ind2 = 0
for i in range(0,s):
    if(xf[i]>tmp2 and xf[i] != tmp1):
      tmp2 = xf[i]
      ind2 = i
m = np.sin(2*int(f[ind1])*p*t)   +  np.sin(2*int(f[ind2])*p*t)
filtered = dawsha - (m)
plt.subplot(3, 2,5)
plt.plot(t,filtered)

xf = fft(filtered)
xf = 2/n * np.abs(xf[0:int(n/2)])

plt.subplot(3, 2,6)
plt.plot(f,xf)
sd.play(filtered, 3*1024)







