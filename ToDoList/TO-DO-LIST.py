tasks = []

def display_menu():
    print("Todo List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View All Tasks")
    print("4. Mark Task as Complete")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

def remove_task():
    display_tasks()
    task_num = int(input("Enter task number to remove: "))
    del tasks[task_num - 1]
    print("Task removed.")

def display_tasks():
    for i, task in enumerate(tasks, start=1):
        status = "X" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")

def mark_task_as_complete():
    display_tasks()
    task_num = int(input("Enter task number to mark as complete: "))
    tasks[task_num - 1]["completed"] = True
    print("Task marked as complete.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            mark_task_as_complete()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Todo List!")

if __name__ == "__main__":
    main()
