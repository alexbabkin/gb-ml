from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 2)
Y = np.arange(-50, 50, 20)
X, Y = np.meshgrid(X, Y)

Z = 2*X + 5*Y - 1
Z2 = 2*X + 5*Y - 150

ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z2)

ax.scatter(0, 0, 0,'z',50,'red')

show()