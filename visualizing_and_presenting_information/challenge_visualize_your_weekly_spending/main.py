import matplotlib.pyplot as plt

def plot_weekly_spending(expenses):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    plt.bar(days, expenses, color="skyblue")
    plt.xlabel("Day of the Week")
    plt.ylabel("Amount Spent ($)")
    plt.title("Weekly Spending Overview")
    plt.tight_layout()
    plt.show()

expenses_example = [45, 20, 30, 50, 25, 60, 40]
plot_weekly_spending(expenses_example)