import math


def print_calc(height: int, width: int, coverage=5):
    no_of_cans = math.ceil((height * width) / coverage)
    print(no_of_cans)


wall_height = int(input("Height of wall :"))
wall_width = int(input("Width of wall : "))
print_calc(wall_height, wall_width)
