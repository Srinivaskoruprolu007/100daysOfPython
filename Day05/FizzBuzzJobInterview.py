print("Fizz Buzz Game")

# Loop through numbers from 1 to 100 (inclusive).
for number in range(1, 101):
    # Check if the number is divisible by both 3 and 5.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check if the number is divisible by 5 only.
    elif number % 5 == 0:
        print("Buzz")
    # Check if the number is divisible by 3 only.
    elif number % 3 == 0:
        print("Fizz")
    # If the number is not divisible by 3 or 5, print the number itself.
    else:
        print(number)