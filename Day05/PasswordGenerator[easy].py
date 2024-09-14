import random

# Define lists of possible characters for the password.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', "#", '$', '%', '^', '&', '*', '(', ')', '_', '+']

print("Welcome to PyPassword Generator!")

# Prompt the user for the number of letters, symbols, and numbers for the password.
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty string to hold the generated password.
password = ""

# Add the specified number of random letters to the password.
for i in range(nr_letters):
    password += letters[random.randint(0, len(letters) - 1)]

# Add the specified number of random symbols to the password.
for i in range(nr_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]

# Add the specified number of random numbers to the password.
for i in range(nr_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]

# Print the generated password.
print(f"Your generated high secured password is {password}")