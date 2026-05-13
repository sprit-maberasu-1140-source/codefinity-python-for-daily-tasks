# Define variables for income and expenses
monthly_income = 3500
rent = 1200
groceries = 400
utilities = 150
transportation = 100
entertainment = 200
other_expenses = 250

def calculate_budget(income, rent, groceries, utilities, transportation, entertainment, other_expenses):
    # 1. 全ての支出を合計する
    total_expenses = rent + groceries + utilities + transportation + entertainment + other_expenses
    # 2. 収入から支出の合計を引いて残高を求める
    remaining_balance = income - total_expenses
    # 3. 合計支出と残高をタプルで返す
    return total_expenses, remaining_balance

# 関数を呼び出して結果を受け取る
total_expenses, remaining_balance = calculate_budget(
    monthly_income, rent, groceries, utilities, transportation, entertainment, other_expenses
)

# フォーマットして出力
budget_summary = f"Total expenses: ${total_expenses}\nRemaining balance: ${remaining_balance}"
print(budget_summary)