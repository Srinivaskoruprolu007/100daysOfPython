# Prompt the user to input a list of student scores separated by spaces.
student_scores = input("Input a list of student scores: ").split()

# Convert each score from string to integer.
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Print the list of student scores to verify conversion.
print(student_scores)

# Initialize a variable to hold the highest score.
heighest = 0

# Iterate over each score in the list to find the highest score.
for score in student_scores:
    # Update the highest score if the current score is greater than the current highest.
    if score > heighest:
        heighest = score

# Print the highest score found among all students.
print(f"The highest score among all students is {heighest}")