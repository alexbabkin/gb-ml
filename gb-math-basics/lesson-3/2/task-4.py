import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


fig, ax = plt.subplots()

x = np.linspace(-2.0, 2.0, 100)
y = np.linspace(-2.0, 2.0, 100)
X, Y = np.meshgrid(x, y)

# circle equation
F = X**2 + Y**2 - 4
ax.contour(X, Y, F, [0])

#circle built-in
circle = plt.Circle((0, 0), 1, fill=False)
ax.add_artist(circle)

# ellipse equation
F = (X ** 2) / 1 + (Y ** 2) / 4 - 1
ax.contour(X, Y, F, [0])

# ellipse built-in
ellipse = Ellipse(xy=(0, 0), width=1, height=5, fc='None', edgecolor='b' , lw=1)
ax.add_patch(ellipse)

# hyperbola equation
F = (X ** 2) / 1 - (Y ** 2) / 4 - 1
ax.contour(X, Y, F, [0])

plt.show()

