#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import random
import scipy as sp
import scipy.interpolate
from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def log_interp(zz,xx,yy,):
    logz = np.log10(zz)
    logx = np.log10(xx)
    logy = np.log10(yy)
    return np.power(10.0, np.interp(logz, logx, logy))

def psd_to_time(freq,amp,numPoints):
  nums = []
  count = 0
  lowFreq = freq[count]
  highFreq = freq[count + 1] # no error checks for now
  lowAmp = amp[count]
  highAmp = amp[count + 1]
  points = np.linspace(freq[0],freq[-1],num=numPoints)
  for j in range(0,numPoints):
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

  yuck = np.zeros(10000)
  duh = np.ones(10000)
  for j in range(1,len(yuck)):
    yuck[j] = np.random.normal(0.0,1.0)
    duh[j] = duh[j] * np.sin(2*3.14159265*100*j/1000)
    yuck[j] = yuck[j] + duh[j]

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

  print("Length of frequency vector is",len(nums))
  gfg_inversed = ifft(complexNums)
  return gfg_inversed, nums
  
# In[3]:

prop_freq = 80 # Hz
prop_amp = 0.00001 # Pa
noise_dB = 60
bandwidth = 40 # Hz
#freq = [20,80,150,200,350,2000]
#amp = [0.01,0.04,0.001,0.001,0.04,0.007042]
freq = [20,prop_freq-bandwidth,prop_freq-bandwidth/2,prop_freq+bandwidth/2,prop_freq+bandwidth,4*prop_freq-bandwidth,4*prop_freq-bandwidth/2,4*prop_freq+bandwidth/2,4*prop_freq+bandwidth,2000]
amp = [1e-9,1e-9,prop_amp,prop_amp,1e-9,1e-9,prop_amp/2,prop_amp/2,1e-9,1e-9]
print("Freq =",freq)
print("Amp =",amp)

# In[4]:


#points = range(freq[0],freq[-1])
numPoints = 1980
timeSeries, nums = psd_to_time(freq,amp,numPoints)
# In[5]:

print("timeSeries type is ",type(timeSeries), "of length =",len(timeSeries))

# In[6]:


plt.plot(timeSeries)
plt.show()


# In[7]:


#plt.loglog(points,nums)
#plt.title('Interppolated PSD')
#plt.show()


# In[8]:

#dummy = fft(yuck)
#print("Class of fft variable is",type(dummy))
#plt.plot(yuck)
#plt.title('Time Series')
#plt.show()
#plt.semilogy(abs(dummy[0:len(dummy)//2]))
#plt.semilogy(abs(dummy))
#plt.title('FFT')
#plt.show()

#gfg_inversed = ifft(dummy)
print("Length of inversed fft =",len(timeSeries))

# In[9]:
#plt.semilogy(nums)
#plt.show()

plt.plot(timeSeries)
plt.title('Time Series from PSD')
plt.show()

print('Length of IFFT result =',len(timeSeries))

dummy = fft(timeSeries)

#plt.semilogy(abs(dummy[0:len(dummy)//2]))
plt.loglog(abs(dummy[0:len(dummy)//2]))
plt.loglog(freq,amp)
plt.title('FFT of inverted time series')
plt.legend(['Processed','Spec'])
plt.show()

# In[ ]:




