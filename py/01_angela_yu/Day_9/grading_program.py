student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for student in student_scores.items():
    grade = ""
    if student[1] > 90:
        grade = "Outstanding"
    elif student[1] > 80:
        grade = "Exceeds Expectations"
    elif student[1] > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student[0]] = grade


print(student_grades)
