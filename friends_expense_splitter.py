def add_person(group):
    name = input("Enter friend's name: ").strip()
    if name in group:
        print("This friend is already in the group.")
    else:
        group[name] = {'paid': 0.0, 'owes': 0.0}
        print(f"{name} added to the group.")

def add_expense(group):
    payer = input("Who paid? ").strip()
    if payer not in group:
        print("This friend is not in the group.")
        return
    try:
        amount = float(input("Enter total amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    # Check if someone can't pay
    skip_person = input("Did anyone not have money to pay? (yes/no): ").strip().lower()
    if skip_person == 'yes':
        person_no_money = input("Who couldn't pay? ").strip()
        if person_no_money not in group:
            print("This friend is not in the group.")
            return
        print(f"{person_no_money}'s share will be covered temporarily.")
    else:
        person_no_money = None

    group[payer]['paid'] += amount
    num_people = len(group)
    share = amount / num_people

    # Split and assign owed amounts
    for person in group:
        if person != payer:
            group[person]['owes'] += share
    if person_no_money:
        group[person_no_money]['owes'] += share
        print(f"{person_no_money} now owes {payer} {share:.2f}")

    print(f"Recorded: {payer} paid {amount:.2f}, split among {num_people} friends.")

def show_balances(group):
    print("\n--- Final Balances ---")
    for person, data in group.items():
        net = data['paid'] - data['owes']
        if net > 0:
            print(f"{person} should receive {net:.2f}")
        elif net < 0:
            print(f"{person} owes {-net:.2f}")
        else:
            print(f"{person} is settled up.")
    print("----------------------\n")

def main():
    group = {}
    while True:
        print("\n1. Add Friend")
        print("2. Add Expense")
        print("3. Show Balances")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_person(group)
        elif choice == '2':
            add_expense(group)
        elif choice == '3':
            show_balances(group)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
