"""Let the user guess a randomly selected number from 1 to 100."""

from random import randint

secret_number = randint(1, 100)
tries = 0
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-100): "))
    tries += 1

    if guess < secret_number:
        print("Too small.")
    elif guess > secret_number:
        print("Too large.")

print(f"Correct! You guessed the number in {tries} tries.")
