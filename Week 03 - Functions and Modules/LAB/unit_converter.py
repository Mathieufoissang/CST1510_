"""Convert between common units in six measurement categories."""


def metres_to_feet(value):
    return value * 3.28084, "feet"


def feet_to_metres(value):
    return value / 3.28084, "metres"


def inches_to_centimetres(value):
    return value * 2.54, "centimetres"


def centimetres_to_inches(value):
    return value / 2.54, "inches"


def miles_to_kilometres(value):
    return value * 1.60934, "kilometres"


def kilometres_to_miles(value):
    return value / 1.60934, "miles"


def convert_length(choice, value):
    if choice == "1":
        return metres_to_feet(value)
    if choice == "2":
        return feet_to_metres(value)
    if choice == "3":
        return inches_to_centimetres(value)
    if choice == "4":
        return centimetres_to_inches(value)
    if choice == "5":
        return miles_to_kilometres(value)
    return kilometres_to_miles(value)


def celsius_to_fahrenheit(value):
    return value * 9 / 5 + 32, "degrees Fahrenheit"


def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9, "degrees Celsius"


def celsius_to_kelvin(value):
    return value + 273.15, "kelvin"


def kelvin_to_celsius(value):
    return value - 273.15, "degrees Celsius"


def convert_temperature(choice, value):
    if choice == "1":
        return celsius_to_fahrenheit(value)
    if choice == "2":
        return fahrenheit_to_celsius(value)
    if choice == "3":
        return celsius_to_kelvin(value)
    return kelvin_to_celsius(value)


def kilograms_to_pounds(value):
    return value * 2.20462, "pounds"


def pounds_to_kilograms(value):
    return value / 2.20462, "kilograms"


def kilograms_to_grams(value):
    return value * 1000, "grams"


def grams_to_kilograms(value):
    return value / 1000, "kilograms"


def convert_mass(choice, value):
    if choice == "1":
        return kilograms_to_pounds(value)
    if choice == "2":
        return pounds_to_kilograms(value)
    if choice == "3":
        return kilograms_to_grams(value)
    return grams_to_kilograms(value)


def gallons_to_litres(value):
    return value * 3.78541, "litres"


def litres_to_gallons(value):
    return value / 3.78541, "US gallons"


def litres_to_millilitres(value):
    return value * 1000, "millilitres"


def millilitres_to_litres(value):
    return value / 1000, "litres"


def convert_volume(choice, value):
    if choice == "1":
        return gallons_to_litres(value)
    if choice == "2":
        return litres_to_gallons(value)
    if choice == "3":
        return litres_to_millilitres(value)
    return millilitres_to_litres(value)


def psi_to_kilopascals(value):
    return value * 6.89476, "kilopascals"


def kilopascals_to_psi(value):
    return value / 6.89476, "psi"


def bar_to_kilopascals(value):
    return value * 100, "kilopascals"


def kilopascals_to_bar(value):
    return value / 100, "bar"


def convert_pressure(choice, value):
    if choice == "1":
        return psi_to_kilopascals(value)
    if choice == "2":
        return kilopascals_to_psi(value)
    if choice == "3":
        return bar_to_kilopascals(value)
    return kilopascals_to_bar(value)


def kilojoules_to_kilocalories(value):
    return value * 0.239006, "kilocalories"


def kilocalories_to_kilojoules(value):
    return value / 0.239006, "kilojoules"


def joules_to_calories(value):
    return value * 0.239006, "calories"


def calories_to_joules(value):
    return value / 0.239006, "joules"


def convert_energy(choice, value):
    if choice == "1":
        return kilojoules_to_kilocalories(value)
    if choice == "2":
        return kilocalories_to_kilojoules(value)
    if choice == "3":
        return joules_to_calories(value)
    return calories_to_joules(value)


def main():
    categories = {
        "1": ("length", convert_length),
        "2": ("temperature", convert_temperature),
        "3": ("mass", convert_mass),
        "4": ("volume", convert_volume),
        "5": ("pressure", convert_pressure),
        "6": ("energy", convert_energy),
    }

    while True:
        print("\nUnit converter: 1) Length  2) Temperature  3) Mass")
        print("               4) Volume  5) Pressure      6) Energy  0) Quit")
        category_choice = input("Choose a category: ").strip()
        if category_choice == "0":
            break
        if category_choice not in categories:
            print("Please choose a category from 1 to 6.")
            continue

        category, conversion_function = categories[category_choice]
        print(f"\n{category.title()} conversions:")
        if category == "length":
            print("1) metres to feet  2) feet to metres  3) inches to centimetres")
            print("4) centimetres to inches  5) miles to kilometres  6) kilometres to miles")
        elif category == "temperature":
            print("1) Celsius to Fahrenheit  2) Fahrenheit to Celsius")
            print("3) Celsius to Kelvin  4) Kelvin to Celsius")
        elif category == "mass":
            print("1) kilograms to pounds  2) pounds to kilograms")
            print("3) kilograms to grams  4) grams to kilograms")
        elif category == "volume":
            print("1) US gallons to litres  2) litres to US gallons")
            print("3) litres to millilitres  4) millilitres to litres")
        elif category == "pressure":
            print("1) psi to kilopascals  2) kilopascals to psi")
            print("3) bar to kilopascals  4) kilopascals to bar")
        else:
            print("1) kilojoules to kilocalories  2) kilocalories to kilojoules")
            print("3) joules to calories  4) calories to joules")

        conversion_choice = input("Choose a conversion: ").strip()
        max_choice = "6" if category == "length" else "4"
        if conversion_choice not in tuple(str(number) for number in range(1, int(max_choice) + 1)):
            print("That conversion is not available.")
            continue

        value = float(input("Enter the value to convert: "))
        result, target_unit = conversion_function(conversion_choice, value)
        print(f"Result: {result:g} {target_unit}")


if __name__ == "__main__":
    main()
