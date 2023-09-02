def prime_checker(number: int):
    isprime = True
    if number < 2:
        isprime = False
    if number == 2:
        isprime = True
    for i in range(3, number):
        if number % i == 0:
            isprime = False
        else:
            isprime = True
    if isprime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


num = int(input("Enter a number to check : "))
prime_checker(num)
