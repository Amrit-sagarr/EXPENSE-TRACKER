print("===== PERSONAL EXPENSE TRACKER =====")

income = float(input("Enter your monthly income: "))
First expense,Second expense,third expense = map(float,input("Enter your expense: ").split())

expenses = First expense + Second expense + third expense
balance = income - expenses

print("Monthly Income:", income)
print("Total Expense:", expense)
print("Remaining Balance:", balance)
