student_scores = input("Input a list of students scores ").split()
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

heighest = 0
for score in student_scores:
    if score > heighest:
        heighest = score

print(f"The heighest score among all students is {heighest}")
