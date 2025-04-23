def intro():
    print("🏞️ You wake up in a mysterious forest")
    print("Two paths lie ahead........")
    print("1️⃣ Take the left path into the dark cave")
    print("2️⃣ Take the right path toward the glowing village")

def cave_path():
    print("\n🦇 You enter the cave. It's cold and dark")
    print("You see a sleeping dragon")
    choice = input("Do you try to steal the treasure (yes/no)? ")

    if choice.lower() == "yes":
        print("The dragon wakes up and breathes fire.....You're toast")
    else:
        print("You sneak away quietly Good choice")

def village_path():
    print("\n You walk into the glowing village")
    print("The villagers welcome you and offer food")
    choice = input("Do you stay overnight (yes/no)? ")

    if choice.lower() == "yes":
        print("You rest well and gain strength for your next adventure")
    else:
        print(" You leave the village and wander under the stars")

def start_game():
    intro()
    path = input("Enter 1 or 2: ")

    if path == "1":
        cave_path()
    elif path == "2":
        village_path()
    else:
        print("The forest swallows you...")

# Start the adventure!
start_game()
