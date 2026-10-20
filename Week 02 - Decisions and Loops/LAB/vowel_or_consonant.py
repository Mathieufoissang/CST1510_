"""Classify a single letter as a vowel or consonant."""

letter = input("Enter one letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single letter of the alphabet.")
elif letter in "aeiou":
    print(f"{letter} is a vowel.")
elif letter == "y":
    print("Sometimes y is a vowel, and sometimes y is a consonant.")
else:
    print(f"{letter} is a consonant.")
