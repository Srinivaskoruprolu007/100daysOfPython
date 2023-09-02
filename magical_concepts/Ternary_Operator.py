# A normal if-elif-else block
age = 25
if age < 18:
    status = 'minor'
elif age < 65:
    status = 'adult'
else:
    status = 'senior'

# Using ternary operator
status = 'minor' if age < 18 else 'adult' if age < 65 else 'senior'
print(status)
