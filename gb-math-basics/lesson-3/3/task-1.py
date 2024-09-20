import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 101)
plt.plot(x, 2 * np.cos(x - 1) + 1)
plt.plot(x, 4 * np.cos(x + 1) + 2)
plt.plot(x, 1 * np.cos(x - 2) + 5)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()