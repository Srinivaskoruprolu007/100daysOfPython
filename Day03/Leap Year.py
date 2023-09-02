Year = int(input("Enter the year you want to check : "))
if Year % 4 == 0:
    if Year % 400 == 0:
        print(f"{Year} is a leap year")
    else:
        print(f"{Year} is not a leap year")
else:
    print(f"{Year} is not a leap year")
