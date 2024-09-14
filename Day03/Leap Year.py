# Leap Year Checker Program

# Get the year from the user and convert it to an integer.
Year = int(input("Enter the year you want to check: "))

# Check if the year is divisible by 4.
if Year % 4 == 0:
    # If divisible by 4, further check if it is divisible by 400.
    if Year % 400 == 0:
        # If divisible by 400, it is a leap year.
        print(f"{Year} is a leap year.")
    else:
        # If not divisible by 400 but divisible by 4, it is not a leap year.
        print(f"{Year} is not a leap year.")
else:
    # If not divisible by 4, it is not a leap year.
    print(f"{Year} is not a leap year.")