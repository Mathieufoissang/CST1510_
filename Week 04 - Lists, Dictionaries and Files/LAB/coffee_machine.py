"""Run a small coffee machine using dictionaries and functions."""


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}


def report():
    """Print the amount of each resource left in the machine."""
    print("\nMachine Resources:")
    for item, amount in resources.items():
        unit = "g" if item == "coffee" else "ml"
        print(f"{item}: {amount}{unit}")


def is_resource_sufficient(ingredients):
    """Return False and explain if the machine lacks an ingredient."""
    for item, amount in ingredients.items():
        if amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, ingredients):
    """Use the ingredients and serve the selected drink."""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")


machine_on = True
print("Welcome to the Coffee Machine!")

while machine_on:
    choice = input(
        "\nWhat would you like? (espresso/latte/cappuccino): "
    ).strip().lower()

    if choice == "off":
        machine_on = False
        print("Coffee machine switched off.")
    elif choice == "report":
        report()
    else:
        # .get() returns None when the drink is not in the menu.
        drink = MENU.get(choice)

        if drink is None:
            print("Sorry, that's not on the menu.")
        elif is_resource_sufficient(drink["ingredients"]):
            cost = drink["cost"]
            print(f"The price is Â£{cost:.2f}")

            try:
                payment = float(input("How much are you paying? Â£"))
            except ValueError:
                print("Please enter a valid amount. Money refunded.")
                continue

            if payment >= cost:
                change = round(payment - cost, 2)
                print(f"Your change is Â£{change:.2f}")
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")

