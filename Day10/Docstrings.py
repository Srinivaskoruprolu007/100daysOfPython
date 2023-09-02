"""
Docstrings are used to document your code and functions
Let's see some examples
"""


def is_leap(year: int) -> bool:
    """
    takes a year a parameter and return true if it is leap
    :param year: int
    :return: bool
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap(2020))