print("===== PERSONAL EXPENSE TRACKER =====")

income = float(input("Enter your monthly income: "))
a =float(input("Enter expense: "))
b =float(input("Enter expense: "))
c=float(input("Enter expense: "))

expense =a+b+c
balance = income - expense

print("Monthly Income:", income)
print("Total Expense:", expense)
print("Remaining Balance:", balance)
