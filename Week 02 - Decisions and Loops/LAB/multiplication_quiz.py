"""Ask the student one randomly generated multiplication question."""

from random import randint

number1 = randint(0, 9)
number2 = randint(0, 9)
answer = int(input(f"What is {number1} * {number2}? "))

if answer == number1 * number2:
    print("Your answer is correct!")
else:
    print(f"Your answer is incorrect. The correct answer is {number1 * number2}.")
