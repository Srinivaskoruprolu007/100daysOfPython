programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again."
}
# Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Name"] = "It's an Identity that everyone got from their "
"birth itself"

# print(programming_dictionary)

# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
for thing in programming_dictionary:
    print(thing)