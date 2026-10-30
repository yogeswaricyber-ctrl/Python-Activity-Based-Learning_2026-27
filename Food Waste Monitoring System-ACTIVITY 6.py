for i in range(3):
    p = int(input("Meals prepared: "))
    s = int(input("Meals served: "))

    left = p - s
    waste = left / p * 100 if p > 0 else 0

    print("Leftovers:", left)
    print("Wastage:", waste, "%")

    if waste > 20:
        print("High wastage")
    else:
        print("Acceptable")