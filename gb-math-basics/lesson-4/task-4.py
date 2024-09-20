import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

a = np.linspace(0.01, 0.02, 1001)
plt.plot(a, 1 * np.pi/a)
plt.plot(a, 2 * np.pi/a)
plt.plot(a, 3 * np.pi/a)
plt.plot(a, 4 * np.pi/a)

x100 = np.empty(1001)
x100.fill(100)

x500 = np.empty(1001)
x500.fill(500)

plt.plot(a, x100)
plt.plot(a, x500)

a1 =  fsolve(lambda a: 2 * np.pi/a - 500, 0.013)
print(a1)

a2 =  fsolve(lambda a: 3 * np.pi/a - 500, 0.019)
print(a2)

plt.show()