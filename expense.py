print("===== PERSONAL EXPENSE TRACKER =====")

income = float(input("Enter your monthly income: "))
First_expense,Second_expense,third_expense = map(float,input("Enter your expense: ").split())

expenses = First_expense + Second_expense + third_expense
balance = income - expenses

print("Monthly Income:", income)
print("Total Expense:", expense)
print("Remaining Balance:", balance)
