# Band Name Generator Program

# The program prompts the user for two inputs:
# 1. The name of the place they grew up.
# 2. The name of their pet.

# It then combines these two inputs to suggest a possible band name.

# Print the title of the program.
print("---Band name generator---")

# Get the name of the place the user grew up.
# The input() function prompts the user and stores the response in the variable `area`.
area = input("Enter the name of the place that you grown up ? ")

# Get the name of the user's pet.
# The input() function prompts the user and stores the response in the variable `pet_name`.
pet_name = input("Enter the name of your pet ? ")

# Combine the area and pet_name to suggest a band name.
# The + operator concatenates the strings with a space in between.
print("Your band name could be " + area + " " + pet_name)