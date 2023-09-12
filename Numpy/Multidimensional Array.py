import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)  # (2, 3)  2 rows and 3 columns

# accessing elements
print(a[0])  # first row
print(a[0, 0])  # first element of the array
print(a[0][0])  # first element of the array

# slicing
print(a[0, :])  # first row
print(a[:, 0])  # first column

# linear algebra
print(np.linalg.inv(a))  # inverse of a

print(np.linalg.det(a))  # determinant of a

print(np.diag(a))  # diagonal elements of an array

print(np.linalg.eig(a))  # to get eigen values and eigen vectors

print(np.linalg.matrix_rank(a))  # rank of the matrix



