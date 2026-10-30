rows = int(input("Rows: "))
columns = int(input("Columns: "))

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if i == 2 and j == 2:
            print("RES", end=" ")
        elif (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()