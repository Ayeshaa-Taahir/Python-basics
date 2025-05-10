def get_input(prompt):
    return input(prompt).strip().lower()

def decision_helper():
    print(" Welcome to the Decision Helper")
    print("This tool helps you decide what task to do based on urgency and importance")

    tasks = []
    while True:
        task_name = input("\nEnter a task (or type 'done' to finish): ")
        if task_name.lower() == "done":
            break
        urgency = get_input("Is it urgent? (yes/no): ")
        importance = get_input("Is it important? (yes/no): ")

        if urgency not in ['yes', 'no'] or importance not in ['yes', 'no']:
            print("Please enter 'yes' or 'no'")
            continue

        tasks.append((task_name, urgency == 'yes', importance == 'yes'))

    print("\n🧩 Here’s your decision breakdown:")

    for task, is_urgent, is_important in tasks:
        if is_urgent and is_important:
            category = "Do it now"
        elif is_important and not is_urgent:
            category = "Schedule it"
        elif is_urgent and not is_important:
            category = "Delegate it"
        else:
            category = "Maybe skip it"

        print(f"- {task.title()} → {category}")

    print("\n Prioritize wisely and stay focused!")

if __name__ == "__main__":
    decision_helper()
