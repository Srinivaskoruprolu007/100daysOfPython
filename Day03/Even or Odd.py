# Even and Odd Number Checker Program

# Print a welcome message for the user.
print("Welcome to Even and Odd Number Checker!")

# Get the number from the user and convert it to an integer.
number = int(input("Which number do you want: "))

# Use the modulus operator (%) to check if the number is even or odd.
# If the number modulo 2 equals 0, it is even.
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    # If the number modulo 2 does not equal 0, it is odd.
    print(f"{number} is an odd number.")