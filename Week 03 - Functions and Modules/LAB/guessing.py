
# Week 3 - Random Number Guessing Game

import random

guess_number = random.randint(1, 100)

print("Guessing Game!")
print("Guess a number between 1 and 100")

while True:

    guess = int(input("Enter your guess: "))

    if guess < guess_number:
        print("low Try again.")

    elif guess > guess_number:
        print("high! Try again.")

    else:
        print("Well done!")
        break
