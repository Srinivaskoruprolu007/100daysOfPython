"""
syntax for List/Dict/Set comprehension
list = [expression for i in iterable if condition]
set = {expression for i in iterable if condition}
dict = {expression for i in iterable if condition}
"""

even_number_list = [i * 2 for i in range(1, 100)]
print(even_number_list)  # [2, 4, 6, 8,....]

set1 = {i for i in range(1, 50)}


"""
prime number in set comprehension
"""
prime_set = {x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))}

for prime in prime_set:
    print(prime)

