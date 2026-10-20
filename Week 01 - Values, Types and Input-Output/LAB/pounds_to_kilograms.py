"""Convert a user-provided weight from pounds to kilograms."""

pounds = float(input("Weight in pounds: "))
kilograms = pounds * 0.454

print(f"{pounds:g} pounds is {kilograms:g} kilograms")
