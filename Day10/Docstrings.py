"""
Docstrings are used to document your code and functions.
Let's see an example where we check if a year is a leap year.
"""


def is_leap(year: int) -> bool:
    """
    Takes a year as a parameter and returns True if it is a leap year, otherwise False.
    
    A leap year:
    - is divisible by 4
    - but if it's divisible by 100, it must also be divisible by 400 to be a leap year.
    
    :param year: int - the year to be checked
    :return: bool - True if the year is a leap year, False otherwise
    """
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 100, check if it's also divisible by 400
        if year % 100 == 0:
            # If divisible by 400, it's a leap year
            if year % 400 == 0:
                return True
            else:
                return False
        # If divisible by 4 but not 100, it's a leap year
        else:
            return True
    # If not divisible by 4, it's not a leap year
    else:
        return False


# Test the function with the year 2020
print(is_leap(2020))  # Output: True (since 2020 is a leap year)