

# Global variable 'enemies' is declared here
enemies = 1

# Local Scope Example
def increase_enemies():
    # 'enemies' is a local variable within this function
    enemies = 2
    print(f"enemies inside function: {enemies}")  # This will print the local value of 'enemies', which is 2

# Calling the function to see the local scope in action
increase_enemies()

# This will print the global 'enemies' variable value, which remains 1
print(f"enemies outside function: {enemies}")

# Local Scope Example in another function
def drink_portion():
    # 'portion_strength' is a local variable within this function
    portion_strength = 2
    print(portion_strength)  # This will print 2, the local variable value

# Calling the function to see the local scope in action
drink_portion()

# Attempting to print 'portion_strength' here would result in an error 
# because 'portion_strength' only exists within the scope of 'drink_portion()'
# Uncommenting the following line would cause an error:
# print(portion_strength)