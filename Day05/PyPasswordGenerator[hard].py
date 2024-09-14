import random

# Define lists of possible characters for the password.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', "#", '$', '%', '^', '&', '*', '(', ')', '_', '+']

print("Welcome to PyPassword Generator!")

# Get user input for the number of letters, symbols, and numbers.
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty list to hold the components of the password.
password = []

# Append the specified number of random letters to the password list.
for i in range(nr_letters):
    password.append(random.choice(letters))

# Append the specified number of random numbers to the password list.
for i in range(nr_numbers):
    password.append(random.choice(numbers))

# Append the specified number of random symbols to the password list.
for i in range(nr_symbols):
    password.append(random.choice(symbols))

# Shuffle the password list to ensure the characters are in random order.
random.shuffle(password)

# Print each character of the shuffled password list without spaces in between.
for letter in password:
    print(letter, end="")