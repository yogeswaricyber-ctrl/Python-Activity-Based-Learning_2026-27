
n = int(input("Enter number of subjects: "))
count = 0

for i in range(n):
    marks = int(input("Enter marks: "))
    attendance = int(input("Enter attendance: "))
    pre = input("Prerequisite completed (yes/no): ")

    if marks >= 40 and attendance >= 75 and pre == "yes":
        print("Pass")
    else:
        print("Requirements Pending")
        count += 1

if count == 0:
    print("Eligible for Next Semester")
else:
    print("Not Eligible for Next Semester")
    print("Pending Subjects:", count)
