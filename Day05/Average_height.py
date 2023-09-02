student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_of_student_heights = 0
for i in range(len(student_heights)):
    sum_of_student_heights += student_heights[i]

avg_student_height = sum_of_student_heights/(len(student_heights))
print(f"The average student's height is {round(avg_student_height)}")
