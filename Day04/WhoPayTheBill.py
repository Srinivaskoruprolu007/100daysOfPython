import random

name_string = input("Give me everybody's names, separated by comma. ")
names = name_string.split(", ")
payer = names[random.randint(0, len(names) - 1)]
print(f"{payer} will be pay the bill.")

# another approach to solve this : using choice in 'random' module
bill_payer = random.choice(names)
print(f"{bill_payer} will be pay the bill.")

