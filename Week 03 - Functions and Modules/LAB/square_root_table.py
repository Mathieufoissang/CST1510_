"""Print square roots for even numbers from 0 through 18."""

from math import sqrt

print(f"{'Number':<12}Square root")
for number in range(0, 20, 2):
    print(f"{number:<12}{sqrt(number):.2f}")
