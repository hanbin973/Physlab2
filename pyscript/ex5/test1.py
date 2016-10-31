import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats

x = np.array([2, 3, 4])
y = np.array([1.83, 1.13, 0.877])

def fit_func(x, a):
	return a * (1/x)

para = curve_fit(fit_func, x, y)
a = para[0]
print (para)

z = fit_func(x, a)

def rsquared(x, y):
	""" Return R^2 where x and y are array-like."""

	slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
	return r_value**2

print (rsquared(y, z))

plt.plot(x, y ,'ro') 
plt.plot(x, fit_func(x, a))
#plt.plot(x, fit_func(x, a, b)+0.1)
plt.axis([0, 5, 0, 2])
plt.ylabel('Magnatic Field (mT)')
plt.xlabel('Distance (cm)')
plt.show()