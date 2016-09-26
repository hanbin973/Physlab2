import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats

x = np.array([1.3,1.2,1.1,1.0,0.9,0.8,0.7])
y = np.array([1.0,1.2,1.4,1.7,2,2.6,3.4])

def fit_func(x, a):
	return a * 1/(x*x)

para = curve_fit(fit_func, x, y)
a = para[0] 
print a

z = fit_func(x, a)

def rsquared(x, y):
	""" Return R^2 where x and y are array-like."""

	slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
	return r_value**2

print rsquared(x, z)

plt.plot(x, y ,'ro') 
plt.plot(x, fit_func(x, a))
plt.axis([0, 2, 0, 5])
plt.ylabel('Weight Loss(g)')
plt.xlabel('Distance between plates(cm)')
plt.show()