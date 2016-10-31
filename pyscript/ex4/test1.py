import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats

x = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
y = np.array([-0.5, -0.9, -1.3, -1.8, -2.4])

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
plt.axis([0, 5, 0, -3])
plt.ylabel('Displacement of Pointer(cm)')
plt.xlabel('Solenoid Current(A)')
plt.show()