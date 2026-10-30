n = int(input("Passengers: "))
total = 0

for i in range(n):
    age = int(input("Age: "))
    d = int(input("Distance: "))
    c = int(input("Class (1-Sleeper, 2-AC, 3-2AC): "))

    rate = c
    fare = d * rate

    if d > 500:
        fare *= 0.8
    elif d > 100:
        fare *= 0.9

    if age < 5:
        fare = 0
    elif age >= 60:
        fare *= 0.8

    fare += 40
    print("Fare:", fare)
    total += fare

print("Total Fare:", total)

if input("Cancel? (yes/no): ").lower() == "yes":
    print("Penalty:", total * 0.25)
    print("Refund:", total * 0.75)