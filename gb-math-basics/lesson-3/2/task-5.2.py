from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import math

fig = figure()
ax = Axes3D(fig)


r = np.arange(0, 5, 0.01)
T = np.arange(0, 2*math.pi, 0.01)

r, T = np.meshgrid(r, T)

X = r*np.cos(T)
Y = r*np.sin(T)
Z = r**2

ax.plot_surface(X, Y, Z)

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(4.*(X**2 + Y**2)/1. + 1)
ax.plot_surface(X, Y, Z)


ax.scatter(0, 0, 0,'z',50,'red')

show()