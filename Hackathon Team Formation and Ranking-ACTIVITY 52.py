n = int(input("Number of teams: "))
teams = []

for i in range(n):
    name = input("Team name: ")
    size = int(input("Team size: "))
    s1 = int(input("Round 1 score: "))
    s2 = int(input("Round 2 score: "))

    if size == 3:
        teams.append([name, s1 + s2, s2])
    else:
        print("Invalid team size")

teams.sort(key=lambda x: (x[1], x[2]), reverse=True)

for i, t in enumerate(teams, 1):
    print(i, t[0], "Score:", t[1])