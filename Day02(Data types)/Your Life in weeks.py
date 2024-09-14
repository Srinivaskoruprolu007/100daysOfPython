# Life Expectancy Calculator
# This program calculates how many days, weeks, and months are left if you live until 90 years old.

# Get the user's current age and convert it to an integer.
age = int(input("What is your current age? \n"))

# Calculate the remaining years until 90.
remaining_years = 90 - age

# Convert the remaining years into days, weeks, and months.
remaining_years_in_days = remaining_years * 365  # Assuming 365 days per year
remaining_years_in_weeks = remaining_years * 52  # Assuming 52 weeks per year
remaining_years_in_months = remaining_years * 12  # 12 months per year

# Print the result using f-strings for formatting.
# This shows how many days, weeks, and months are left.
print(f"You have {remaining_years_in_days} days, {remaining_years_in_weeks} weeks, and {remaining_years_in_months} months left.")