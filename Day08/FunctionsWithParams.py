# Function to greet with a name
def greet(name: str):
    """
    Greets the user with a good morning message.
    
    Parameters:
    name (str): The name of the person to greet.
    """
    print(f"Hello Good morning {name}")

# Function to calculate and print the total of two numbers
def total(number1: int, number2: int):
    """
    Prints the total of two numbers.
    
    Parameters:
    number1 (int): The first number.
    number2 (int): The second number.
    """
    print(f'The total of {number1} and {number2} is {number2 + number1}')

# Example usage of total function
total(56, 7)

# Function to greet with a name and location
def greet_with(name: str, location: str):
    """
    Greets the user with their name and asks about their location.
    
    Parameters:
    name (str): The name of the person to greet.
    location (str): The location to ask about.
    """
    print(f'Hello {name}')
    print(f'What is it like in {location}')

# Example usage of greet_with function
greet_with("sri", "Vizag")