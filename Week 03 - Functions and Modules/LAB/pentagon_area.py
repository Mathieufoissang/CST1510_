"""Calculate the area of a regular pentagon from its side length."""

from math import pi, tan

side = float(input("Enter the pentagon's side length: "))

if side < 0:
    print("Side length cannot be negative.")
else:
    area = 5 * side ** 2 / (4 * tan(pi / 5))
    print(f"Area = {area:.2f}")
