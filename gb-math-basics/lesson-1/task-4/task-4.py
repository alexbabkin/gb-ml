import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 121)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(2*x))
plt.show()