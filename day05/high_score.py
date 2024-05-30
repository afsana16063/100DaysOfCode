# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max = 0
for student_score in student_scores:
  if student_score > max:
    max = student_score

print(f"The highest score in the class is: {max}")