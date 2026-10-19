"""## Coffee Machine

**Uses:** dictionaries, nested dicts, `.get()`, `.items()`, functions
(Week 3), `while` loops

A simulated coffee machine with a fixed menu and finite resources.

**Set up the data**

1. Create a dict called `resources`:
   ```python
   resources = {"water": 300, "milk": 200, "coffee": 100}
   ```
   (Water and milk are in ml, coffee is in g.)
2. Create the menu as a dict of dicts:
   ```python
   MENU = {
       "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
       "latte":    {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
       "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
   }
   ```

**Write the functions**

3. Define a function called `report()`.
4. Inside it, loop over `resources.items()` and print each resource and
   its amount, for example `water: 300`.
5. Define a function called `is_resource_sufficient(ingredients)`.
6. Inside it, write a loop: `for item, amount in ingredients.items():`
7. Inside the loop, if `amount > resources[item]`:
   - print `f"Sorry, there is not enough {item}."`
   - return `False`
8. After the loop (not inside it), return `True`.
9. Define a function called `make_coffee(drink_name, ingredients)`.
10. Inside it, loop over `ingredients.items()` and subtract each
    `amount` from the matching resource: `resources[item] -= amount`.
11. After the loop, print `f"Here is your {drink_name}. Enjoy!"`

**Write the main loop**

12. Outside the functions, create a variable `machine_on` and set it to
    `True`.
13. Start a `while machine_on:` loop.
14. Inside the loop, ask
    `"What would you like? (espresso/latte/cappuccino):"` and store the
    answer in `choice`.
15. If `choice == "off"`, set `machine_on = False`.
16. Add an `elif choice == "report":` that calls `report()`.
17. Add an `else:`. Inside it, look up the drink with
    `drink = MENU.get(choice)`.
18. If `drink` is `None`, print `"Sorry, that's not on the menu."`
19. Otherwise, call `is_resource_sufficient(drink["ingredients"])`. If it
    returns `True`:
    - print the price using `drink["cost"]`
    - ask the user how much they are paying, convert it with `float()`,
      and store it in `payment`
    - if `payment >= drink["cost"]`, work out
      `change = round(payment - drink["cost"], 2)`, print the change, then
      call `make_coffee(choice, drink["ingredients"])`
    - otherwise, print `"Sorry, that's not enough money. Money refunded."`
20. Run the program and order lattes until the machine runs out of
    something. Check that it tells you what's missing. Then type
    `report` and `off` to test the extra commands."""


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
    print("\nMachine Resources:")
    for item, amount in resources.items():
        unit = "g" if item == "coffee" else "ml"
        print(f"{item}: {amount}{unit}")


def is_resource_sufficient(ingredients):
    for item, amount in ingredients.items():
        if amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, ingredients):
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

