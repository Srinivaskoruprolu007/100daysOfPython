# Integer Manipulation in Python

# round() function:
# The division 8 / 3 results in a float.
# The round() function rounds the result to 1 decimal place.
# In this case, 8 / 3 = 2.6667, which gets rounded to 2.7.
print(round(8 / 3, 1))  # Output: 2.7

# Floor Division (//):
# Floor division (//) returns the largest integer less than or equal to the result.
# 8 // 3 returns 2, which is the integer part of the division.
print(round(8 // 3))  # Output: 2

# f-strings for formatted output:
# f-strings allow embedding expressions inside string literals.
# Variables `score`, `height`, and `isWinning` are inserted into the string using { }.
score = 150
height = 1.5
isWinning = True

# The following prints a formatted string with the values of the variables.
print(f"your score is {score}, your height is {height} , your is {isWinning}")

# Output: your score is 150, your height is 1.5, your is True