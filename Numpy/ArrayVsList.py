import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

l = l + [4]
print(l)
a = a + np.array([4])
print(a)

l = l * 2
print(l)
a = a * np.array([2])
print(a)
"""
In list operation done by entire list
but in array, operations done by each and every element
"""

# mathematical operations
a = np.sqrt(a)
print(a)

a = np.abs(a)
print(a)

a = np.floor(a)
print(a)

a = np.log(a)
print(a)
