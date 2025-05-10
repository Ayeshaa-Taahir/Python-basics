def northern_trip_planner():
    exchange_rate = 280  # 1 USD = 280 PKR

    places = {
        "Hunza Valley": {
            "activity": "Sightseeing & Photography",
            "solo_budget": 18000,
            "agency_budget": 22000,
            "history": "Hunza Valley is famous for its ancient forts like Baltit and Altit and breathtaking Karakoram mountains",
            "famous_spots": "Eagle's Nest, Passu Cones, and Attabad Lake",
            "dishes": "Chapshuro, Dawdo soup, and Buckwheat bread"
        },
        "Skardu": {
            "activity": "Trekking & Camping",
            "solo_budget": 22000,
            "agency_budget": 26000,
            "history": "Skardu is the gateway to the world's highest peaks including K2, and has a rich Balti culture",
            "famous_spots": "Shangrila Resort, Shigar Fort, and Satpara Lake",
            "dishes": "Balti Gosht, Momos (dumplings), and Apricot soup"
        },
        "Swat Valley": {
            "activity": "River Rafting & Hiking",
            "solo_budget": 14000,
            "agency_budget": 17000,
            "history": "Swat was once called the Switzerland of the East and is rich in Buddhist heritage",
            "famous_spots": "Malam Jabba, Fizagat Park, and Mingora Bazaar",
            "dishes": "Chapli Kebab, Trout fish, and Lamb Karahi"
        },
        "Naran Kaghan": {
            "activity": "Lake Visit & Boating",
            "solo_budget": 16000,
            "agency_budget": 19000,
            "history": "Naran Kaghan is famous for the fairy tale-like Saif-ul-Malook Lake and beautiful meadows",
            "famous_spots": "Saif-ul-Malook Lake, Babusar Top, and Lalazar",
            "dishes": "Trout fish, Mutton Karahi, and Chapli Kebab"
        },
        "Fairy Meadows": {
            "activity": "Hiking & Bonfire",
            "solo_budget": 20000,
            "agency_budget": 24000,
            "history": "Fairy Meadows is the base camp of Nanga Parbat and is considered one of the most scenic places in Pakistan",
            "famous_spots": "Nanga Parbat Base Camp and Raikot Bridge",
            "dishes": "Local mountain herbs stew and grilled trout"
        },
        "Murree": {
            "activity": "Chair Lift & Mall Road",
            "solo_budget": 10000,
            "agency_budget": 13000,
            "history": "Murree is a colonial-era hill station, popular for its pine forests and cool weather",
            "famous_spots": "Mall Road, Patriata, and Kashmir Point",
            "dishes": "Makki ki Roti with Saag and local sweets"
        },
    }

    print("Welcome to the Northern Pakistan Trip Planner\n")
    print("Choose from these beautiful places\n")

    for idx, place in enumerate(places, 1):
        print(f"{idx}. {place}")

    choice = input("\nEnter the numbers or names of your destinations : ").strip().lower()
    selected_places = []

    # Process multiple inputs
    choices = [c.strip() for c in choice.split(",")]
    for ch in choices:
        if ch.isdigit():
            idx = int(ch)
            if 1 <= idx <= len(places):
                place_name = list(places.keys())[idx - 1]
                if place_name not in selected_places:
                    selected_places.append(place_name)
        else:
            for place in places:
                if ch in place.lower():
                    if place not in selected_places:
                        selected_places.append(place)
                    break

    if not selected_places:
        print("No valid destinations selected. Please try again")
        return

    is_foreigner = input("\nAre you a foreigner visiting Pakistan for the first time? (yes/no): ").strip().lower()

    print("\nWho are you traveling with?")
    print("1. Alone")
    print("2. Friends")
    print("3. Family")
    print("4. Agency")

    travel_input = input("\nEnter the number or name of your choice: ").strip().lower()

    travel_options = {
        '1': 'alone', 'alone': 'alone',
        '2': 'friends', 'friends': 'friends',
        '3': 'family', 'family': 'family',
        '4': 'agency', 'agency': 'agency'
    }

    travel_type = travel_options.get(travel_input)

    if not travel_type:
        print("\nInvalid option selected")
        return

    print("\nHere’s your trip plan:\n")

    for place in selected_places:
        details = places[place]
        print(f"Destination: {place}")
        print(f"Top Activity: {details['activity']}")

        if travel_type == 'alone':
            budget = details['solo_budget']
            print(f"Estimated budget for a solo trip: {budget} PKR")
            if is_foreigner == 'yes':
                print(f"Approx in USD: {budget / exchange_rate:.2f} USD")

        elif travel_type == 'friends':
            people = int(input(f"\nHow many friends are going to {place} (including you)? "))
            total_budget = details['solo_budget'] * 0.8 * people
            per_person = total_budget / people
            print(f"Total budget for the group: {total_budget:.0f} PKR")
            print(f"Each friend should contribute: {per_person:.0f} PKR")
            if is_foreigner == 'yes':
                print(f"Total in USD: {total_budget / exchange_rate:.2f} USD")
                print(f"Per person in USD: {per_person / exchange_rate:.2f} USD")

        elif travel_type == 'family':
            family_members = int(input(f"\nHow many family members are going to {place} (including you)? "))
            total_budget = details['solo_budget'] * 0.85 * family_members
            per_person = total_budget / family_members
            print(f"Total budget for your family: {total_budget:.0f} PKR")
            print(f"Approx per person: {per_person:.0f} PKR")
            if is_foreigner == 'yes':
                print(f"Total in USD: {total_budget / exchange_rate:.2f} USD")
                print(f"Per person in USD: {per_person / exchange_rate:.2f} USD")

        elif travel_type == 'agency':
            budget = details['agency_budget']
            print(f"Estimated budget via travel agency: {budget} PKR")
            if is_foreigner == 'yes':
                print(f"Approx in USD: {budget / exchange_rate:.2f} USD")

        print(f"\nHistory: {details['history']}")
        print(f"Famous Spots: {details['famous_spots']}")
        print(f"Popular Dishes: {details['dishes']}")
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    northern_trip_planner()
