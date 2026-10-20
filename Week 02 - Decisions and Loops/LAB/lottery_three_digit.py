"""Play the three-digit lottery described in the exercise."""

from random import randint

lottery = f"{randint(0, 999):03d}"
guess = input("Enter a three-digit number: ").strip()

if guess.isdigit() and len(guess) <= 3:
    guess = guess.zfill(3)
    if guess == lottery:
        prize = 10000
    elif sorted(guess) == sorted(lottery):
        prize = 3000
    elif any(digit in lottery for digit in guess):
        prize = 1000
    else:
        prize = 0
    print(f"Lottery number: {lottery}")
    print(f"Your prize is £{prize:,}.")
else:
    print("Please enter a number from 000 to 999.")
