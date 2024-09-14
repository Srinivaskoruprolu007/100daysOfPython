# Function to determine if a year is a leap year.
def is_leap(year: int) -> bool:
    # If the year is divisible by 4, it's a leap year, unless...
    if year % 4 == 0:
        # If the year is divisible by 100, it has to also be divisible by 400 to be a leap year.
        if year % 100 == 0:
            # If divisible by 400, it's a leap year.
            if year % 400 == 0:
                return True
            else:
                return False
        # If divisible by 4 but not 100, it's a leap year.
        else:
            return True
    # If not divisible by 4, it's not a leap year.
    else:
        return False


# Function to determine the number of days in a given month of a given year.
def days_in_month(year: int, month: int) -> int:
    # Check if the input year is less than 1900 or month is greater than 12 (invalid input).
    if year < 1900 or month > 12:
        return 0
    # If it's a leap year, use 29 days for February.
    elif is_leap(year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # If not a leap year, use 28 days for February.
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Return the number of days for the given month (subtract 1 because list index starts from 0).
    return month_days[month-1]


# Get the year and month input from the user.
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Call the days_in_month function and store the result in the 'days' variable.
days = days_in_month(year, month)

# Print the number of days in the given month and year.
print(days)