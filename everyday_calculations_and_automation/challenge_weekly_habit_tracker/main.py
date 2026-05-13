def track_habit(daily_values):
    # Write your code here
    total = 0
    for value in daily_values:
        total += value
    average = total/len(daily_values)
    print("Weekly Total:",total)
    print("Weekly Average:",average)
    

# Sample calls
track_habit([8, 7, 6, 9, 8, 7, 10])
track_habit([2, 2, 2, 2, 2, 2, 2])
