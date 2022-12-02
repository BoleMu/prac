incomes = []
total = 0
month = int(input("How many months? "))
print()

for i in range(1, month + 1):
    income = float(input(f"Enter income for month {i}: "))
    incomes.append(income)

print("\nIncome Report\n", "-" * 11)
for m in range(1, month + 1):
    income = incomes[m - 1]
    total += income
    print(f"Month {m} - Income: $ {income:10.2f}      Total: $ {total:10.2f}")