import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats

x = np.array([0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0])
y = np.array([0, 0.1, 0.6, 1.3, 2.4, 3.9, 5.6])

def fit_func(x, a):
	return a * x * x

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
plt.axis([0, 10, 0, 6])
plt.ylabel('Weight Loss(g)')
plt.xlabel('Voltage(kV)')
plt.show()