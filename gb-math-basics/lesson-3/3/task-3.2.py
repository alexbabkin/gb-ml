import numpy as np
import matplotlib.pyplot as plt

fi = np.linspace(0, 2*np.pi, 101)
r = np.empty(101)
r.fill(1)

plt.polar(fi, r)
plt.show()