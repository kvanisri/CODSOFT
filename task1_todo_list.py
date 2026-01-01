tasks = []

def show_menu():
    print("\n----- TO DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "status": "Pending"})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {task['status']}")

def complete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark as completed: "))
            tasks[num - 1]["status"] = "Completed"
            print("Task marked as completed.")
        except:
            print("Invalid input.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            removed_task = tasks.pop(num - 1)
            print(f"Deleted task: {removed_task['task']}")
        except:
            print("Invalid input.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Thank you!")
        break
    else:
        print("Please choose a valid option.")
