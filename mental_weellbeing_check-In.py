import datetime
import random

mood_quotes = {
    "happy": [
        "Keep shining, the world needs your light",
        "Happiness is contagious, spread it around"
    ],
    "sad": [
        "It's okay to feel sad — even the moon goes through phases",
        "Crying doesn’t mean you’re weak, it means you’ve been strong for too long"
    ],
    "anxious": [
        "Breathe — you’ve survived 100% of your worst days",
        "You are more than your worries"
    ],
    "neutral": [
        "A calm mind brings inner strength",
        "Stillness is sometimes the best move"
    ]
}

self_care_suggestions = [
    "Drink a glass of water and stretch",
    "Write down 3 things you're grateful for",
    "Take a 10-minute walk outside",
    "Listen to your favorite calming song",
    "Text someone just to say hi"
]

def get_user_mood():
    print("Welcome to your daily mental wellbeing check-in")
    print("How are you feeling today?")
    print("1. Happy\n2. Sad\n3. Anxious\n4. Neutral")
    
    mood_input = input("Enter the number that best matches your mood: ")
    mood_map = {"1": "happy", "2": "sad", "3": "anxious", "4": "neutral"}
    
    mood = mood_map.get(mood_input)
    if not mood:
        print("Invalid input. Please run again.")
        return None
    return mood

def offer_support(mood):
    print("\nHere's something for you today")
    print("Quote:", random.choice(mood_quotes[mood]))
    print("Suggestion:", random.choice(self_care_suggestions))

def write_journal():
    journal = input("\nWould you like to write a short journal entry today? (yes/no): ").lower()
    if journal == "yes":
        entry = input("Write your thoughts here: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        with open("mental_journal.txt", "a") as file:
            file.write(f"{date}: {entry}\n")
        print("Your entry has been saved")
    else:
        print("No problem, maybe next time")

def main():
    mood = get_user_mood()
    if mood:
        offer_support(mood)
        write_journal()
        print("\nTake care of yourself. You matter")

if __name__ == "__main__":
    main()
