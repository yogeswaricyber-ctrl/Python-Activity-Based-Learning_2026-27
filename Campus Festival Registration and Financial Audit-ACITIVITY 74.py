participants = ["Ravi", "Sita", "Ravi", "Ram"]
fees = 4 * 500
sponsorship = 2000
expenses = 3000

print("Participants:", set(participants))
print("Duplicate registrations:", len(participants) - len(set(participants)))

balance = fees + sponsorship - expenses
print("Final balance: ₹", balance)