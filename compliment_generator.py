import random

def get_compliments():
    return {
        "default": [
            "You’re an absolute star!",
            "You’re doing amazing, keep it up!",
            "The world’s a better place with you in it!",
            "Your smile could light up a city!",
            "You have a brilliant mind!",
            "You’re cooler than a penguin in sunglasses!"
        ],
        "happy": [
            "Your happiness is contagious!",
            "You spread sunshine wherever you go!",
            "You glow with positivity!"
        ],
        "sad": [
            "Sending you a virtual hug",
            "You’re stronger than you think",
            "Remember, tough times don’t last — you do!"
        ],
        "stressed": [
            "Breathe in… breathe out… you’ve got this",
            "One step at a time, superstar!",
            "Even superheroes need a break sometimes"
        ]
    }

def main():
    compliments = get_compliments()
    name = input("Hi! What’s your name? ")
    mood = input(f"Nice to meet you, {name}! How are you feeling today (happy, sad, stressed)? ").lower()

    if mood in compliments:
        compliment = random.choice(compliments[mood])
    else:
        compliment = random.choice(compliments["default"])

    print(f"\nHey {name}, {compliment}")

if __name__ == "__main__":
    main()
