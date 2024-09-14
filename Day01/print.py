import sys

# Basic Print Statement:
# This prints the string "Hello World !" to the console.
# The print() function outputs whatever is passed to it as a string.
print("Hello World !")

# Printing Multiple Lines:
# The \n represents a newline character, causing the text after it to be printed on the next line.
print("Hello World ! \nHello World !")

# Using `sep` Parameter in `print`:
# The `sep` parameter specifies how to separate the values. By default, the separator is a space " ".
# In this case, sep="@" will print Hello@gmail.com.
print("Hello", "gmail.com", sep="@")

# String Concatenation:
# The `+` operator is used to concatenate two strings without adding any space.
# Output: "Hello Srinivas"
print("Hello" + " Srinivas")

# Concatenation with User Input:
# The input() function prompts the user for input.
# The value provided by the user is concatenated with "Hello " and printed.
# Example: If the user inputs "Srinivas", the output would be `Hello Srinivas`.
print("Hello " + input("What is your name ?"))

# Getting the Length of a String (with Memory Size):
# The input() function stores the user-provided value in the variable `name`.
# The sys.getsizeof() function returns the size of an object in memory (in bytes).
# This doesn't return the length of the string but rather the memory size occupied by the string object.
name = input("Enter your name ?")
size = sys.getsizeof(name)
print(size)