# Program to count and display the number of characters in a name

# Ask the user for their name and calculate the length of the input string.
# The len() function returns the number of characters in the input string.
num_char = len(input("What is your name?\n"))

# Convert the number of characters (an integer) to a string so it can be concatenated with other strings.
new_num_char = str(num_char)

# Print a message displaying the number of characters in the name.
# The concatenated string includes the number of characters.
print("Your name has " + new_num_char + " characters.")