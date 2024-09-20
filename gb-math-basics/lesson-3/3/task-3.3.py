import numpy as np
import matplotlib.pyplot as plt

fi = np.linspace(-np.pi/6, 0, 101)
r = 2  / np.cos(fi + np.pi/6)

plt.polar(fi, r)
plt.show()