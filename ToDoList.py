import json
import os
from colorama import init, Fore, Style

init(autoreset=True)

TASKS_FILE = 'tasks.json'


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(Fore.GREEN + "Task added!")


def view_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = Fore.GREEN + "✔" if task["completed"] else Fore.RED + "✘"
        print(f"{i}. {task['task']} [{status}]")


def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print(Fore.GREEN + "Task marked as completed!")
        else:
            print(Fore.RED + "Invalid task number.")
    except ValueError:
        print(Fore.RED + "Invalid input.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(Fore.GREEN + f"Deleted task: {removed['task']}")
        else:
            print(Fore.RED + "Invalid task number.")
    except ValueError:
        print(Fore.RED + "Invalid input.")


def main():
    tasks = load_tasks()
    while True:
        print("\n" + Fore.CYAN + "==== To-Do List Menu ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print(Fore.CYAN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
