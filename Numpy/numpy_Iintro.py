# to import the module
import numpy as np
# to get the version of the numpy
print(np.__version__)

# let's create an array with numpy
a = np.array([1, 2, 3])
print(a)

# to check the shape of the array
print(a.shape)

# to check the data type of element in array
print(a.dtype)

# to check the dimension of the array
print(a.ndim)

# to check the size of the array
print(a.size)

# to get the size of each element in bytes
print(a.itemsize)

b = a * np.array([2, 0, 2])
print(b)