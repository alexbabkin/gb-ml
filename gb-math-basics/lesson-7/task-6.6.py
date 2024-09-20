import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])

Q, R = np.linalg.qr(A)

print(Q)
print(R)

print(np.dot(Q, R))
print(np.dot(np.transpose(Q), Q))

R1 = R[:2, :2]
print(R1)

B1 = np.dot(np.transpose(Q), B)[:2]

X1 = np.linalg.solve(R1, B1)
print(X1)

X = np.append(X1, 0)