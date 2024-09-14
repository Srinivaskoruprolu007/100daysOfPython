# Pizza Delivery Bill Calculator

# Print a welcome message for the user.
print("Welcome to Python Pizza Deliveries!")

# Get the size of the pizza from the user.
# The size input is used to determine the base price of the pizza.
size = input("What size do you want? S, M, or L ")

# Initialize the bill to 0.
bill = 0

# Determine the base price based on the size of the pizza.
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Ask the user if they want pepperoni.
add_pepperoni = input("Do you want pepperoni? Y or N ")

# Add the cost of pepperoni to the bill if the user wants it.
if add_pepperoni == "Y":
    bill += 2

# Ask the user if they want extra cheese.
extra_cheese = input("Do you want extra cheese? Y or N ")

# Add the cost of extra cheese to the bill if the user wants it.
if extra_cheese == "Y":
    bill += 1

# Print the total bill for the pizza.
print(f"Your total bill for your pizza is ${bill}")