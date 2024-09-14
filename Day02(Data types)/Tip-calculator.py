# Tip Calculator Program

# Print a welcome message for the user.
print("Welcome to the tip calculator.")

# Get the total bill amount from the user and convert it to a float.
bill = float(input("What was the total bill? $"))

# Ask the user for the percentage of tip they want to give and convert it to an integer.
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15 ?"))

# Ask for the number of people who will split the bill and convert it to an integer.
people_count = int(input("How many people want to split the bill ?"))

# Calculate the tip amount by multiplying the bill with the tip percentage divided by 100.
tip = bill * (percentage_tip / 100)

# Calculate the total bill by adding the tip to the original bill.
total_bill = tip + bill

# Divide the total bill by the number of people to get each person's share.
# The round() function is used to round the result to 2 decimal places.
each_person_split = round((total_bill / people_count), 2)

# Print the amount each person should pay using f-string formatting.
print(f"Each person should pay: ${each_person_split}")