def get_outfit(temp_celsius, condition):
    condition = condition.lower()

    if temp_celsius < 0:
        outfit = "heavy jacket, thermal layers, gloves, and boots"
    elif 0 <= temp_celsius < 10:
        outfit = "jacket, warm pants, and a scarf"
    elif 10 <= temp_celsius < 20:
        outfit = "light sweater or hoodie with jeans"
    elif 20 <= temp_celsius < 30:
        outfit = "t-shirt, light pants or shorts"
    else:
        outfit = "sleeveless shirt, shorts, and drink lots of water"

    if "rain" in condition:
        outfit += " plus a raincoat or umbrella"
    elif "snow" in condition:
        outfit += " and wear waterproof boots for snow"
    elif "sun" in condition or "clear" in condition:
        outfit += " and don’t forget sunglasses"

    return outfit

def main():
    print("What Should You Wear Today?")
    try:
        temp = float(input("Enter the temperature in Celsius: "))
        condition = input("What’s the weather like? (e.g., sunny, rainy, snowy): ")

        recommendation = get_outfit(temp, condition)
        print("\n Based on the weather, you should wear:")
        print(f" {recommendation}")
    except ValueError:
        print("Please enter a valid number for temperature.")

if __name__ == "__main__":
    main()