"""Play the two-digit lottery described in the exercise."""

from random import randint

lottery = f"{randint(0, 99):02d}"
guess = input("Enter a two-digit number: ").strip()

if guess.isdigit() and len(guess) <= 2:
    guess = guess.zfill(2)
    if guess == lottery:
        prize = 10000
    elif sorted(guess) == sorted(lottery):
        prize = 3000
    elif guess[0] in lottery or guess[1] in lottery:
        prize = 1000
    else:
        prize = 0
    print(f"Lottery number: {lottery}")
    print(f"Your prize is £{prize:,}.")
else:
    print("Please enter a number from 00 to 99.")
