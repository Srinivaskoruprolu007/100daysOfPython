print("Welcome to the rollercoaster Ride!")
height = int(input("What is your height in cm :"))
if height > 120:
    print("Yes you can go to the rollercoaster ride ")
    age = int(input("whats is your age "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")
    want_photo = input("Do you want a photo taken ? Y or N. ")
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride ")
