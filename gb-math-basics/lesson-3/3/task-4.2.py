import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

x = np.linspace(-2, 4.25, 1001)


plt.plot(x, np.exp(x) + x * (1 - x**2 + 1) - 1)

plt.show()

def equation(x):
    return math.exp(x) + x * (1 - x**2 + 1) - 1

x1 = fsolve(equation, -1.5)
x2 = fsolve(equation, 0)
x3 = fsolve(equation, 1.5)
x4 = fsolve(equation, 4)

print(x1, x2, x3, x4)

# result:
# x < -1.58183535; 0 < x < 1.50237837; x > 4.2
# y = x^2 - 1