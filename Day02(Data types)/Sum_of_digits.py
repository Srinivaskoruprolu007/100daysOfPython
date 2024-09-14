# Program to add the digits of a two-digit number

# Ask the user to input a two-digit number and convert it to an integer.
two_digit_number = int(input("Type a two-digit number: "))

# Convert the integer back to a string to access its individual digits.
new_two_digit_number = str(two_digit_number)

# Extract the first digit by accessing the first character of the string and convert it back to an integer.
first_digit = int(new_two_digit_number[0])

# Extract the second digit by accessing the second character of the string and convert it back to an integer.
second_digit = int(new_two_digit_number[1])

# Calculate the total by adding the first and second digits.
total = first_digit + second_digit

# Print the result.
print(total)