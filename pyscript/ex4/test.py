import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats

x = np.array([0,0.3,0.5,0.75,1.0,1.25,1.5,1.75,2.0])
y = np.array([0.2, 0.0, -0.1, -0.4, -0.6, -0.8, -1.2, -1.4, -1.7])

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

print (rsquared(x, z))

plt.plot(x, y ,'ro') 
plt.plot(x, fit_func(x, a, b)-0.1)
plt.plot(x, fit_func(x, a, b)+0.1)
plt.axis([0, 5, 1, -2])
plt.ylabel('Displacement of Pointer(cm)')
plt.xlabel('Current Balance Current(A)')
plt.show()