
n = int(input("Number of students: "))
students = []

for i in range(n):
    name = input("Name: ")
    marks = int(input("Aggregate marks: "))
    s1 = int(input("Subject 1 marks: "))
    s2 = int(input("Subject 2 marks: "))
    att = int(input("Attendance %: "))
    income = int(input("Family income: "))

    if marks >= 75 and s1 >= 40 and s2 >= 40 and att >= 75 and income <= 200000:
        students.append((marks, name))

students.sort(reverse=True)

print("Eligible Students (Rank List):")
for rank, (marks, name) in enumerate(students, 1):
    print(rank, name, marks)

