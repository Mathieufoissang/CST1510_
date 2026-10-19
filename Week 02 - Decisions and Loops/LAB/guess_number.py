"""Number Guessing Game

Uses: ``while``, comparisons, ``if``/``elif``/``else``

1. Pick a secret number and store it in a variable (hard-code it for now
   — no ``random`` yet).
2. Loop: ask the user to guess. If their guess is too high, say so. Too
   low, say so. Correct, congratulate them and stop the loop.
3. Count how many guesses it took.

Revisit this in Week 3: once you've met the ``random`` module, swap the
hard-coded secret number for ``random.randint(1, 100)`` — same game, now a
different number every time.

Adapted from: 100 Days of Code, Day 12.
"""

secret_number = 42
guess_count = 0

guess = int(input("Guess the secret number (1–100): "))
guess_count += 1

while guess != secret_number:
    if guess > secret_number:
        print("Too high. Try again.")
    elif guess < secret_number:
        print("Too low. Try again.")

    guess = int(input("Guess again: "))
    guess_count += 1

print(f"Correct! You guessed the number in {guess_count} guesses.")