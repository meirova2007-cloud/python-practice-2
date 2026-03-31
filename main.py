name = input("Enter student name: ")
math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python = float(input("Enter Python grade: "))

average = (math + physics + python) / 3

if average >= 90:
    letter_grade = 'A'
elif average >= 75:
    letter_grade = 'B'
elif average >= 60:
    letter_grade = 'C'
elif average >= 50:
    letter_grade = 'D'
else:
    letter_grade = 'F'

scholarship = average >= 70 and math >= 70 and physics >= 70 and python >= 70

print("================================")
print("Student :", name.upper())
print("Math :", math)
print("Physics :", physics)
print("Python :", python)
print("--------------------------------")
print("Average :", round(average, 1))
print("Letter grade :", letter_grade)
print("Scholarship :", scholarship)
print("================================")

grades = [math, physics, python]
subjects = ['Math', 'Physics', 'Python']

for i in range(len(subjects)):
    grade = grades[i]
    if grade >= 90:
        comment = 'Excellent'
    elif grade >= 75:
        comment = 'Good'
    elif grade >= 60:
        comment = 'Satisfactory'
    else:
        comment = 'Fail'
    print(subjects[i], ":", grade, "->", comment)

print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))
masked_name = name.replace(name[0], '*', 1)
print("Masked name :", masked_name)