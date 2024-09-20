import numpy as np
import scipy.linalg as la

A = np.array([ [1, 2, 3], [2, 16, 21], [4, 28, 73] ])
P, L, U = la.lu(A)

print(la.det(A))

print(P)
print(L)
print(U)

print(A - np.dot(P, np.dot(L, U)))
print(np.dot(np.linalg.inv(P), A) - np.dot(L, U)) # вероятно в уроке ошибка, LU-разложение, это разложение вида A = P L U, а не A P = L U

B = np.array([1, 2, 3])
s = np.linalg.solve(A, B)
print(s)