# calculator

# addition
def add(a: int, b: int) -> int:
    return a + b


# subtraction
def subtract(a: int, b: int) -> int:
    return a - b


# multiplication
def multiply(a: int, b: int) -> int:
    return a * b


# division
def divide(a: int, b: int) -> int:
    return a / b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():

    num1 = float(input("What's the first number?: "))

    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:

        operator = input('Pick an operation from the line above: ')
        num2 = float(input("What's the another number?: "))
        calculation_funtion = operations[operator]
        answer = calculation_funtion(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        choice = input(f"Type 'Y' to continue calculating with {answer} or 'N' to exit :").lower()

        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
