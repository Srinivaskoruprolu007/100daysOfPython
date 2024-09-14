# BMI Calculator Program

# Ask the user for their height in meters and store it as a string.
height = input("Enter the height in m: ")

# Ask the user for their weight in kilograms and store it as a string.
weight = input("Enter the weight in kg: ")

# Convert the height and weight from strings to floats for mathematical operations.
# BMI formula: weight (kg) / height (m)^2
BMI = float(weight) / float(height) ** 2

# Print the BMI value as an integer by converting it using int().
# This removes any decimal places and shows only the whole number part of the BMI.
print(int(BMI))