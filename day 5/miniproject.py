tasks = input("Enter your tasks separated by commas: ").split(",")

for task in tasks:
    print(f"🔔 Reminder: Don't forget to {task.strip()}!")
