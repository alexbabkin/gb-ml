import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.linalg.det(A)) #6.66133814775094e-16

B = np.array([12, 2, 1])
s = np.linalg.lstsq(A, B)
print(s) 
print(np.dot(A, [-7.69444444, -0.61111111,  6.47222222])) #[10.5         5.00000001 -0.49999998]

B = np.array([3, 2, 1])
s = np.linalg.lstsq(A, B)
print(s)

print(np.dot(A, [-1.94444444, -0.11111111,  1.72222222])) # [3.         2.00000001 1.00000002]