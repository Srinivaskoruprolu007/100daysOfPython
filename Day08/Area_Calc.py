import math

def print_calc(height: int, width: int, coverage: int = 5):
    """
    Calculates and prints the number of paint cans required to cover a wall.

    Parameters:
    height (int): The height of the wall in meters.
    width (int): The width of the wall in meters.
    coverage (int, optional): The coverage area of one can of paint in square meters. Defaults to 5.
    """
    # Calculate the area of the wall
    area = height * width
    
    # Calculate the number of cans needed, rounding up to ensure complete coverage
    no_of_cans = math.ceil(area / coverage)
    
    # Print the number of cans required
    print(f"Number of cans required: {no_of_cans}")

# Input from user
wall_height = int(input("Height of wall (in meters): "))
wall_width = int(input("Width of wall (in meters): "))

# Function call
print_calc(wall_height, wall_width)