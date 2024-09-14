# Roller Coaster Height Checker

# Print a welcome message for the user.
print("Welcome to the Roller Coaster!")

# Get the height of the user in centimeters and convert it to an integer.
height = int(input("What is your height in cm? "))

# Check if the height is equal to or greater than 120 cm.
if height >= 120:
    # If the height is 120 cm or more, the user can ride the roller coaster.
    print("You can ride the roller coaster!")
else:
    # If the height is less than 120 cm, the user cannot ride the roller coaster.
    print("Sorry, you have to grow taller before you can ride.")