print("Welcome to the tip calculator. ")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15 ?"))
people_count = int(input("How many people want to split the bill ?"))
tip = bill * (percentage_tip /100)
total_bill = tip + bill
each_person_split = round((total_bill / people_count), 2)
print(f"Each person should pay: ${ each_person_split }")
