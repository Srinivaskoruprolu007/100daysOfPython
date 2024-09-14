# BMI Calculator 2.0

# Print a welcome message for the user.
print("Welcome to BMI calculator 2.0")

# Get the user's height in meters and convert it to a float.
height = float(input("Enter your height in m: "))

# Get the user's weight in kilograms and convert it to an integer.
weight = int(input("Enter your weight in kg: "))

# Calculate BMI using the formula: weight (kg) / height (m)^2
# Round the result to the nearest integer.
BMI = round(weight / (height ** 2))

# Determine the BMI category based on the calculated BMI value and print the result.
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