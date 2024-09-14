# Prompt the user to input a list of student heights separated by spaces.
student_heights = input("Input a list of student heights: ").split()

# Convert each height in the list from string to integer.
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Print the list of student heights to verify conversion.
print(student_heights)

# Initialize a variable to hold the sum of student heights.
sum_of_student_heights = 0

# Iterate over the list of student heights and calculate the total sum.
for i in range(len(student_heights)):
    sum_of_student_heights += student_heights[i]

# Calculate the average height by dividing the total sum by the number of students.
avg_student_height = sum_of_student_heights / len(student_heights)

# Print the average height, rounded to the nearest whole number.
print(f"The average student's height is {round(avg_student_height)}")