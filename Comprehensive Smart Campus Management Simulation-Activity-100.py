
students = []
attendance = []
marks = []
events = []
resources = ("Library", "Lab", "Ground")

while True:
    print("\n1.Add Student  2.Attendance")
    print("3.Marks  4.Event  5.Resources  6.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        students.append(input("Enter name: "))

    elif ch == 2:
        attendance.append(input("Present/Absent: "))

    elif ch == 3:
        marks.append(int(input("Enter marks: ")))

    elif ch == 4:
        events.append(input("Enter event: "))

    elif ch == 5:
        for r in resources:
            print(r)

    elif ch == 6:
        print("Students:", students)
        print("Attendance:", attendance)
        print("Marks:", marks)
        print("Events:", events)
        break

    else:
        print("Invalid Choice")
