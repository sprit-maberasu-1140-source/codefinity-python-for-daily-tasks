def add_task(tasks, task):
    # リストの最後にタスクを入れるよ
    tasks.append(task)

def remove_task(tasks, task):
    # タスクがリストにあるか確かめて、あったら消すよ
    if task in tasks:
        tasks.remove(task)

def print_tasks(tasks):
    # 今のタスクをぜんぶ見せるよ
    print(tasks)

tasks = []
add_task(tasks, "Buy groceries")
add_task(tasks, "Call the bank")
add_task(tasks, "Walk the dog")
print_tasks(tasks)           # → ['Buy groceries', 'Call the bank', 'Walk the dog']
remove_task(tasks, "Call the bank")
print_tasks(tasks)           # → ['Buy groceries', 'Walk the dog']