def print_expense_report(expenses):
    print("Item         | Amount")
    print("-------------|-------")
    total = 0.0
    for item, amount in expenses:
        line = f"{item:<12} | ${amount:>6.2f}"
        print(line)
        total += amount
    print("-------------|-------")
    total_line = f"{'Total':<12} | ${total:>6.2f}"
    print(total_line)

expenses = [
    ("Groceries", 54.32),
    ("Utilities", 120.00),
    ("Coffee", 8.50),
    ("Internet", 45.99)
]
print_expense_report(expenses)