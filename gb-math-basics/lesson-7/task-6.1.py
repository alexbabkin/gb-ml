import numpy as np

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
s = np.linalg.solve(A, B)

print(s)
# [-9.2         0.9         6.46666667]