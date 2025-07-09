tasks = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task removed successfully: {task}")
    else:
        print("Task not found")

def show_tasks():
    if tasks:
        print("Remaining tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "4":
        # Save tasks before exiting
        save_tasks()
        print("Exiting...")
        break
    else:
        print("Invalid option, please choose again.")