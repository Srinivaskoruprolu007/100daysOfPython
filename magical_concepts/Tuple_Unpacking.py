"""
we can use tuple unpacking to assign multiple values in one go
"""

student = ('Srinivas', 23, 'Machine Learning')
name, age, course = student
print(name)  # Srinivas
print(age)  # 23
print(course)  # Machine Learning

"""
we can add '*' in front of variable to unpack everything else into one variable
"""

fruits = ['mango', 'apple', 'Guava', 'pineapple', 'Papaya']
first_fruit, second_fruit, *other = fruits

print(first_fruit)
print(second_fruit)
print(other)

