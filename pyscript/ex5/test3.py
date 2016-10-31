import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats

x = np.array([0.05 * (i+1) for i in range(5)])
y = np.array([-2.85, -5.96, -8.88, -11.65, -14.34])

def fit_func(x, a, b):
	return a * x + b

para = curve_fit(fit_func, x, y)
a = para[0][0]
b = para[0][1]
print (para)

z = fit_func(x, a, b)

def rsquared(x, y):
	""" Return R^2 where x and y are array-like."""

	slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
	return r_value**2

print (rsquared(y, z))

plt.plot(x, y ,'ro') 
plt.plot(x, fit_func(x, a, b))
#plt.plot(x, fit_func(x, a, b)+0.1)
plt.axis([0, 0.5, 0, -25])
plt.ylabel('Magnatic Field (mT)')
plt.xlabel('Current (A)')
plt.show()