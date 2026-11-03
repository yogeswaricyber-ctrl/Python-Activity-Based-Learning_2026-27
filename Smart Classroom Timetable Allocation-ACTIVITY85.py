courses = [("Python", 40, 1), ("AI", 30, 2)]
rooms = [("Room 8", 50), ("Room 9", 35)]
assigned = []

for c, students, period in courses:
    for r, capacity in rooms:
        if capacity >= students and (r, period) not in assigned:
            assigned.append((r, period))
            print(c, "->", r, "Period", period)
            break
    else:
        print(c, "Cannot be allocated")