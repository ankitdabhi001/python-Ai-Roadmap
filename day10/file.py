# Read and display tasks from todo.txt

try:
    with open("todo.txt", "r") as file:
        tasks = file.readlines()

    if tasks:
        print("📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    else:
        print("✅ Your to-do list is empty!")

except FileNotFoundError:
    print("⚠️ todo.txt file not found. Please create one first.")
