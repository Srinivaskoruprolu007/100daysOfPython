# Dictionary with student names and their scores
student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Neville': 62,
}

# Create an empty dictionary to store student grades
student_grades = {}

# Iterate through each student in the student_scores dictionary
for key in student_scores:
    # Get the score for the current student
    score = student_scores[key]
    
    # Determine the grade based on the score and assign it to the student_grades dictionary
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# Print the dictionary containing student names and their respective grades
print(student_grades)