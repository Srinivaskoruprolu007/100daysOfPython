print("Welcome to BMI calculator 2.0 ")
height = float(input("Enter your height in m : "))
weight = int(input("Enter your weight in kg: "))

BMI = round((weight / (height ** 2)))
if BMI <= 18.5:
    print(f"Your BMI is {BMI}, You are underweight")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}, You are normal weight")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI}, You are overweight")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI}, You are obese")
else:
    print(f"Your BMI is {BMI}, Clinically obese")
