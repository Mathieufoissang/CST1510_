"""Print a number's multiplication table from 0 through 9."""

number = int(input("Enter a number: "))

for multiplier in range(10):
    print(f"{multiplier} x {number} = {multiplier * number}")
