import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def Q(x, y, z):
    return(x**2 + y**2 + z**2)

X = np.arange(0, 2, 0.1)
Y = np.arange(-2, 0, 0.1) # Y тоже можно выразить (тогда наверное получится линия в 3D - граница пересечения 2х поверхностей), но мне кажется не обязательно
X, Y = np.meshgrid(X, Y)

fig = figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Q(X, Y, X + 2*Y - 1))

show()

A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])

s = np.linalg.lstsq(A, B)
print(s)