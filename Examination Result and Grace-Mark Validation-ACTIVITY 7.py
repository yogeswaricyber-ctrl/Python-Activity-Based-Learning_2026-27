
n = int(input("Number of subjects: "))
marks = []

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

grace = 5

for i in range(n):
    if marks[i] < 35 and 35 - marks[i] <= grace:
        marks[i] = min(35, marks[i] + grace)

print("Final Marks:", marks)

if all(m >= 35 for m in marks):
    avg = sum(marks) / n
    if avg >= 75:
        print("Distinction")
    elif avg >= 60:
        print("First Class")
    elif avg >= 50:
        print("Second Class")
    else:
        print("Pass")
else:
    print("Fail")
