def chatbot():
    print("Hi! I'm Eyesha Let's chat (Type 'bye' to exit)")

    memory = {}
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("Eyesha: Bye! It is nice listening to you, even though I never listen to anyone -_-")
            break
        elif "your name" in user_input:
            print("Eyesha: I'm Eyesha, your Python-powered buddy.")
        elif "my name is" in user_input:
            name = user_input.split("my name is")[-1].strip().capitalize()
            memory["name"] = name
            print(f"Eyesha: Nice to meet you, {name}!")
        elif "how are you" in user_input:
            print("Eyesha: Though I'm just code, but I'm feeling ilogical")
        elif "i am" in user_input:
            mood = user_input.split("i am")[-1].strip()
            memory["mood"] = mood
            print(f"Eyesha: I hope your '{mood}' day gets even better")
        elif "what's my name" in user_input or "what is my name" in user_input:
            if "name" in memory:
                print(f"Eyesha: Your name is {memory['name']}, of course")
            else:
                print("Eyesha: Hmm, I don't think you told me your name yet")
        elif "how am i" in user_input:
            if "mood" in memory:
                print(f"Eyesha: You said you were feeling {memory['mood']} earlier.")
            else:
                print("Eyesha: Not sure! You tell me ")
        else:
            print("Eyesha: Interesting......Tell me more!")

chatbot()
