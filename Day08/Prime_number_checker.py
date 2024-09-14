def prime_checker(number: int):
    """
    Checks if a number is prime and prints the result.
    
    Parameters:
    number (int): The number to check.
    """
    # Edge cases
    if number < 2:
        print(f"{number} is not a prime number")
        return
    if number == 2:
        print(f"{number} is a prime number")
        return
    
    # Check for factors from 2 up to the square root of the number
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

# Example usage
num = int(input("Enter a number to check: "))
prime_checker(num)