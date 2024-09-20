import numpy as np
import itertools
from math import factorial
from math import pow

k, n = 0, 100000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(k, n, k/n)

def calc_comp(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print(calc_comp(4, 2) / pow(2, 4))