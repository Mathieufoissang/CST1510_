"""Report the percentage of password characters guessed in the right place."""

actual_password = "MDX123"
guess = input("Guess the password: ")

if guess == actual_password:
    print("Password cracked!")
else:
    matching_positions = 0
    positions_to_check = min(len(actual_password), len(guess))

    for position in range(positions_to_check):
        if guess[position] == actual_password[position]:
            matching_positions += 1

    accuracy = matching_positions / len(actual_password) * 100
    print(f"Accuracy: {accuracy:.0f}%")
