import json
import random

def load_responses():
    with open('responses.json', 'r') as f:
        return json.load(f)

def chat_with_bot(responses):
    print("🤖 Hi! I’m MoodBot. How are you feeling today?")
    print("Type 'exit' anytime to quit.\n")
    while True:
        user_input = input("👤 You: ").lower()
        if user_input in ["exit", "quit", "bye"]:
            print("🤖 Bot: Take care! 💛 See you soon!")
            break
        found_mood = False
        for mood, replies in responses.items():
            if mood in user_input:
                print(f"🤖 Bot: {random.choice(replies)}")
                found_mood = True
                break
        if not found_mood:
            print("🤖 Bot: Hmm, I’m not sure how to respond — but I’m here for you!")

if __name__ == "__main__":
    responses = load_responses()
    chat_with_bot(responses)
