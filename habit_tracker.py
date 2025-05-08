import json
from datetime import datetime

DATA_FILE = 'habits.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_habit(habits):
    name = input("Enter the name of the new habit: ").strip()
    if name in habits:
        print("Habit already exists")
    else:
        habits[name] = {'dates': []}
        print(f"Habit '{name}' added")

def mark_habit(habits):
    name = input("Enter the habit to mark as done: ").strip()
    if name not in habits:
        print("Habit not found.")
        return
    today = datetime.now().strftime('%Y-%m-%d')
    if today in habits[name]['dates']:
        print("You already marked this habit today")
    else:
        habits[name]['dates'].append(today)
        print(f"Habit '{name}' marked as done for today!")

def show_progress(habits):
    if not habits:
        print("No habits to track")
        return
    print("\n--- Habit Progress ---")
    for habit, info in habits.items():
        count = len(info['dates'])
        print(f"{habit}: completed {count} time(s)")
    print("-----------------------\n")

def main():
    habits = load_data()
    while True:
        print("\n1. Add Habit")
        print("2. Mark Habit as Done Today")
        print("3. Show Progress")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            mark_habit(habits)
        elif choice == '3':
            show_progress(habits)
        elif choice == '4':
            save_data(habits)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
