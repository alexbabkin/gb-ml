from scipy.optimize import fsolve
import math

def equations(p):
    x, y = p
    return (x**2 - 1 - y, math.exp(x) + x * (1 - y) -1)

x, y =  fsolve(equations, (4, 15))
print(x, y)
print(equations((x, y)))