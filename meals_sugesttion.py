# Sample meal suggestions based on ingredients
meal_suggestions = {
    "eggs": ["Omelette", "Boiled Eggs", "French Toast"],
    "bread": ["Sandwich", "Garlic Bread", "Bread Pizza"],
    "tomato": ["Tomato Soup", "Pasta", "Tomato Chutney"],
    "cheese": ["Grilled Cheese", "Mac & Cheese", "Cheesy Pasta"],
    "potato": ["Fries", "Mashed Potatoes", "Potato Curry"],
    "chicken": ["Grilled Chicken", "Chicken Curry", "Chicken Sandwich"],
    "rice": ["Fried Rice", "Rice Bowl", "Chicken Biryani"],
    "milk": ["Cereal", "Milkshake", "Porridge"],
    "banana": ["Banana Shake", "Pancakes", "Banana Bread"]
}

def get_suggestions(fridge_items):
    possible_meals = []
    for item in fridge_items:
        if item in meal_suggestions:
            possible_meals.extend(meal_suggestions[item])
    return list(set(possible_meals))

def smart_fridge():
    print(" Welcome to the Smart Fridge Assistant")
    print("Tell me what's in your fridge and I'll suggest meals you can cook")

    items = input("\nEnter the items in your fridge (comma-separated): ").lower().split(',')
    cleaned_items = [item.strip() for item in items]

    suggestions = get_suggestions(cleaned_items)

    if suggestions:
        print("\nBased on what you have, you can make:")
        for meal in suggestions:
            print(f"- {meal}")
    else:
        print("\nSorry, I couldn't find any matching recipes with the current items")

if __name__ == "__main__":
    smart_fridge()
