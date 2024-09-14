# Mathematical Operators in Python

# Addition: Adds two numbers.
print(3 + 4)  # Output: 7

# Subtraction: Subtracts the second number from the first.
print(3 - 4)  # Output: -1

# Multiplication: Multiplies two numbers.
print(3 * 4)  # Output: 12

# Division: Divides the first number by the second and returns a float.
print(3 / 4)  # Output: 0.75

# Exponentiation: Raises the first number to the power of the second.
print(3 ** 4)  # Output: 81 (3 raised to the power of 4)

# PEDMASLR stands for the order of operations in Python:
'''
1. Parentheses ()
2. Exponents **
3. Multiplication * and Division / (left to right)
4. Addition + and Subtraction - (left to right)
'''

# Example to demonstrate PEDMASLR:
# Breakdown:
# 1. 3 * 3 = 9 (Multiplication)
# 2. 3 / 3 = 1 (Division)
# 3. 9 + 1 = 10 (Addition)
# 4. 10 - 3 = 7 (Subtraction)
print(3 * 3 + 3 / 3 - 3)  # Output: 7