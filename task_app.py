# task_app.py

# load task from file at start
def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
tasks = load_tasks()

def show_menu():
    print("\n=== Task App ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("4. Reset Tasks")

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def reset_tasks():
    confirm = input("Are you sure you want to reset all tasks? (yes/no): ")
    if confirm.lower() == 'yes':
        open('tasks.txt', 'w').close()
        tasks.clear()
        print("All tasks deleted")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    elif choice == "4":
        reset_tasks()
    
    else:
        print("Invalid choice. Try again.")
    
