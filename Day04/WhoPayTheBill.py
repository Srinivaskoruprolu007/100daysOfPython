import random

# Prompt the user to input names separated by commas.
name_string = input("Give me everybody's names, separated by comma: ")

# Split the input string into a list of names.
names = name_string.split(", ")

# Randomly select a person to pay the bill using the randint function.
payer = names[random.randint(0, len(names) - 1)]
print(f"{payer} will pay the bill.")

# Another approach: Randomly select a person using the choice function.
bill_payer = random.choice(names)
print(f"{bill_payer} will pay the bill.")