# Define a dictionary with some initial key-value pairs
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# Retrieving an item from the dictionary
# print(programming_dictionary["Bug"])  # Uncomment to print the definition of "Bug"

# Adding a new item to the dictionary
# Note: Concatenated string should be on one line to avoid syntax issues
programming_dictionary["Name"] = "It's an Identity that everyone got from their birth itself"

# print(programming_dictionary)  # Uncomment to print the updated dictionary

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary (uncomment the lines below to clear the dictionary)
# programming_dictionary = {}
# print(programming_dictionary)  # Uncomment to print the now-empty dictionary

# Edit an item in the dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)  # Uncomment to print the updated dictionary

# Loop through the dictionary and print each key
for thing in programming_dictionary:
    print(thing)