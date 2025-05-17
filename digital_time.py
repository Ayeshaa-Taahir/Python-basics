import json
import datetime
import os

def save_time_capsule():
    name = input("What’s your name? ")
    message = input("Write a message to your future self: ")
    date_str = input("Enter the date to unlock the message (YYYY-MM-DD): ")

    try:
        unlock_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        capsule = {
            "name": name,
            "message": message,
            "unlock_date": date_str
        }

        filename = f"{name.lower().replace(' ', '_')}_capsule.json"
        with open(filename, "w") as f:
            json.dump(capsule, f)
        print("\n Your message is sealed and waiting in the future...\n")
    except ValueError:
        print(" Invalid date format. Please use YYYY-MM-DD.")

def open_time_capsule():
    name = input("Enter your name to open your capsule: ")
    filename = f"{name.lower().replace(' ', '_')}_capsule.json"

    if not os.path.exists(filename):
        print(" No capsule found with that name.")
        return

    with open(filename, "r") as f:
        capsule = json.load(f)
        unlock_date = datetime.datetime.strptime(capsule["unlock_date"], "%Y-%m-%d").date()
        today = datetime.date.today()

        if today >= unlock_date:
            print(f"\n Message from your past self:\n\"{capsule['message']}\"")
        else:
            days_remaining = (unlock_date - today).days
            print(f"\n Not yet! {days_remaining} days left until you can read your message.")

def main():
    print(" Welcome to the Digital Time Capsule")
    print("1. Write a message to the future")
    print("2. Open a saved message\n")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        save_time_capsule()
    elif choice == "2":
        open_time_capsule()
    else:
        print(" Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
