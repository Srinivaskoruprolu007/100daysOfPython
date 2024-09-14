# Calculator Program

# Addition function
def add(a: int, b: int) -> int:
    return a + b

# Subtraction function
def subtract(a: int, b: int) -> int:
    return a - b

# Multiplication function
def multiply(a: int, b: int) -> int:
    return a * b

# Division function
def divide(a: int, b: int) -> int:
    return a / b

# Dictionary to store the operations and their corresponding functions.
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Calculator logic
def calculator():

    # Get the first number from the user
    num1 = float(input("What's the first number?: "))

    # Print available operations
    for operator in operations:
        print(operator)

    should_continue = True

    # Loop to continue calculating if the user wants to
    while should_continue:

        # Get the operation and the second number from the user
        operator = input('Pick an operation from the line above: ')
        num2 = float(input("What's the another number?: "))

        # Retrieve the appropriate function from the operations dictionary
        calculation_funtion = operations[operator]
        answer = calculation_funtion(num1, num2)

        # Display the result
        print(f"{num1} {operator} {num2} = {answer}")

        # Ask if the user wants to continue with the current result or exit
        choice = input(f"Type 'Y' to continue calculating with {answer} or 'N' to exit :").lower()

        if choice == 'y':
            # If 'Y', use the result as the next 'num1'
            num1 = answer
        else:
            # If 'N', stop the loop and restart the calculator
            should_continue = False
            calculator()

# Call the calculator function to start the program
calculator()