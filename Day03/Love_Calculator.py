# Love Score Calculator Program

# Get the names of both people from user input.
Her = input("Enter her name: ")
Him = input("Enter his name: ")

# Combine both names into a single string.
Together = Her + Him

# Convert the combined names to lowercase to ensure case-insensitive counting.
Together_lower = Together.lower()

# Count the occurrences of each letter in the word "TRUE".
t = Together_lower.count("t")
r = Together_lower.count("r")
u = Together_lower.count("u")
e = Together_lower.count("e")

# Calculate the "TRUE" score by summing the counts of 't', 'r', 'u', and 'e'.
true = t + r + u + e

# Count the occurrences of each letter in the word "LOVE".
l = Together_lower.count("l")
o = Together_lower.count("o")
v = Together_lower.count("v")
e = Together_lower.count("e")

# Calculate the "LOVE" score by summing the counts of 'l', 'o', 'v', and 'e'.
love = l + o + v + e

# Form the final love score by concatenating the "TRUE" and "LOVE" scores.
love_score = int(str(true) + str(love))

# Determine the message to display based on the love score.
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")