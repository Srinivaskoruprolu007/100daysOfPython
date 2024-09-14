# Roller Coaster Ride Ticket Calculator

# Print a welcome message for the user.
print("Welcome to the Roller Coaster Ride!")

# Get the user's height in centimeters and convert it to an integer.
height = int(input("What is your height in cm: "))

# Check if the user is tall enough to ride the roller coaster.
if height > 120:
    # If the user is tall enough, print a message allowing them to ride.
    print("Yes, you can go on the roller coaster ride!")
    
    # Get the user's age and convert it to an integer.
    age = int(input("What is your age? "))
    
    # Determine the ticket price based on age.
    if age < 12:
        # If the user is under 12, set the ticket price to $5.
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        # If the user is between 12 and 18, set the ticket price to $7.
        bill = 7
        print(f"Youth tickets are ${bill}")
    else:
        # If the user is 19 or older, set the ticket price to $12.
        bill = 12
        print(f"Adult tickets are ${bill}")
    
    # Ask if the user wants a photo taken and store their response.
    want_photo = input("Do you want a photo taken? Y or N: ")
    
    # If the user wants a photo, add $3 to the bill.
    if want_photo == "Y":
        bill += 3
    
    # Print the final bill amount.
    print(f"Your final bill is ${bill}")
else:
    # If the user is not tall enough, print a message indicating they cannot ride.
    print("Sorry, you have to grow taller before you can ride.")