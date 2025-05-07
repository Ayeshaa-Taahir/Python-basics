def get_expenses():
    num_people = int(input("How many people are sharing expenses? "))
    people = []
    expenses = {}

    for i in range(num_people):
        name = input(f"Enter the name of person {i + 1}: ")
        people.append(name)
        amount = float(input(f"Enter how much {name} paid: "))
        expenses[name] = amount

    return people, expenses

def calculate_split(people, expenses):
    total = sum(expenses.values())
    share = total / len(people)

    balances = {}
    for person in people:
        balances[person] = expenses[person] - share

    return total, share, balances

def print_results(total, share, balances):
    print("\n------ Expense Summary ------")
    print(f"Total expense: {total:.2f}")
    print(f"Each person should pay: {share:.2f}\n")
    print("Settlements:")

    for person, balance in balances.items():
        if balance > 0:
            print(f"{person} should receive {balance:.2f}")
        elif balance < 0:
            print(f"{person} should pay {-balance:.2f}")
        else:
            print(f"{person} is settled up.")

def main():
    print("Welcome to the Expense Splitter!")
    people, expenses = get_expenses()
    total, share, balances = calculate_split(people, expenses)
    print_results(total, share, balances)

if __name__ == "__main__":
    main()
