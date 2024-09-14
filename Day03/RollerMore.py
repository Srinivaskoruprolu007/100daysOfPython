# Roller Coaster Ticket Pricing Program

# Print a welcome message for the user.
print("Welcome to Roller Coaster!")

# Get the user's height in centimeters and convert it to an integer.
height = int(input("What is your height in cm: "))

# Check if the user is tall enough to ride the roller coaster.
if height >= 120:
    # If the user is tall enough, print a message allowing them to ride.
    print("You can ride the roller coaster!")

    # Get the user's age and convert it to an integer.
    age = int(input("What is your age? "))

    # Determine the ticket price based on the user's age.
    if age < 12:
        # If the user is under 12, the ticket price is $5.
        print("Please pay $5.")
    elif age <= 18:
        # If the user is between 12 and 18, the ticket price is $7.
        print("Please pay $7.")
    else:
        # If the user is 19 or older, the ticket price is $12.
        print("Please pay $12.")
else:
    # If the user is not tall enough, print a message indicating they cannot ride.
    print("Sorry, you have to grow taller before you can ride.")