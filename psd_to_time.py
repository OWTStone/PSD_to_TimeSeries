#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import random
import scipy as sp
import scipy.interpolate
from scipy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def log_interp(zz,xx,yy,):
    logz = np.log10(zz)
    logx = np.log10(xx)
    logy = np.log10(yy)
    return np.power(10.0, np.interp(logz, logx, logy))


# In[3]:


freq = [0,19,20,80,150,200,350,2000]
amp = [1e-7,1e-7,0.01,0.04,0.001,0.001,0.04,0.007042]
numPoints = 50000

# In[4]:


#points = range(freq[0],freq[-1])
points = np.linspace(freq[0],freq[-1],num=numPoints+1)
print(points)
# In[5]:


nums = []
count = 0
lowFreq = freq[count]
highFreq = freq[count + 1] # no error checks for now
lowAmp = amp[count]
highAmp = amp[count + 1]
for j in range(0,len(points)):
    if points[j] == highFreq:
        temp = highAmp
    else:
      if points[j] > highFreq:
        count = count + 1
        lowFreq = freq[count]
        highFreq = freq[count + 1] # no error checks for now
        lowAmp = amp[count]
        highAmp = amp[count + 1]
      temp = log_interp(points[j],[lowFreq,highFreq],[lowAmp,highAmp])
    nums.append(temp)


# In[6]:


plt.plot(points,nums)
plt.show()


# In[7]:


plt.loglog(points,nums)
plt.title('Interpolated PSD')
plt.show()


halfRange = len(nums)
print(halfRange)
for j in range(1,halfRange):
  #print(halfRange-j+1)
  temp = nums[halfRange-j]
  nums.append(temp)

complexNums = []
for j in range(0,len(nums)):
  randomPhase = 2*np.pi*np.random.uniform(0,1)
  complexNums.append(complex(nums[j]*np.sin(randomPhase),nums[j]*np.cos(randomPhase)))


gfg_inversed = ifft(complexNums)
#gfg_inversed = ifft(dummy)
print("Length of inversed fft =",len(gfg_inversed))
print("Length of frequency vector is",len(points))
# In[9]:
plt.semilogy(nums)
plt.show()

plt.plot(gfg_inversed.real)
plt.title('Time Series from PSD')
plt.show()

print('Length of IFFT result =',len(gfg_inversed))

dummy = fft(gfg_inversed.real)
dummyFreqs = fftfreq(len(dummy)*2,1/numPoints)
print("Length of frequency vector =",len(dummyFreqs))
#plt.semilogy(abs(dummy[0:len(dummy)//2]))
plt.loglog(points,abs(dummy[0:len(dummy)//2+1]))
plt.loglog(freq,amp)
plt.title('FFT of inverted time series')
plt.legend(['Calculated','Spec'])
plt.show()
print("Freqs =",dummyFreqs)
# In[ ]:

