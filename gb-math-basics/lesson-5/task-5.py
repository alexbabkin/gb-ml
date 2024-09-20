import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from math import sqrt

n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
plt.plot([0, 1], [b, a + b])
plt.show()

xm = np.mean(x)
ym = np.mean(y)

xi_xm = x - xm
yi_ym = y - ym

R = sum(xi_xm * yi_ym) / sqrt(sum(xi_xm ** 2) * sum(yi_ym ** 2))
print(R)
