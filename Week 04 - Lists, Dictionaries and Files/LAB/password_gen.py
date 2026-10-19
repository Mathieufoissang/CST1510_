"""Generate passwords from a requested number of characters.
## Password Generator

**Uses:** lists, `random.choice()`, `random.shuffle()`, `for` loops,
string building

1. At the top of your file, write `import random`.
2. Create a list called `letters` containing every letter `a`â€“`z` and
   `A`â€“`Z` as separate strings, for example `["a", "b", "c", ...]`.
3. Create a list called `numbers` containing the strings `"0"` to `"9"`.
4. Create a list called `symbols` containing some symbols, for example
   `["!", "#", "$", "%", "&", "(", ")", "*", "+"]`.
5. Use `input()` to ask how many letters the user wants. Convert it with
   `int()` and store it in `nr_letters`.
6. Do the same for symbols, storing the answer in `nr_symbols`.
7. Do the same for numbers, storing the answer in `nr_numbers`.

**Easy version â€” letters, then symbols, then numbers**

8. Create a variable `password` and set it to an empty string `""`.
9. Write a `for` loop using `range(nr_letters)`. Inside it, add
   `random.choice(letters)` to the end of `password` using `+=`.
10. Write a second `for` loop using `range(nr_symbols)` that does the
    same with `symbols`.
11. Write a third `for` loop using `range(nr_numbers)` that does the
    same with `numbers`.
12. Print `password`.

**Hard version â€” shuffled order**

13. Create a variable `password_list` and set it to an empty list `[]`.
14. Repeat steps 9â€“11, but this time use `.append()` to add each random
    character to `password_list` instead of adding it to a string.
15. Call `random.shuffle(password_list)` to mix up the order.
    (Note: `shuffle()` changes the list in place and returns `None`, so
    don't write `password_list = random.shuffle(password_list)`.)
16. Create a variable `password` and set it to `""`.
17. Write a `for char in password_list:` loop that adds each `char` to
    `password`.
18. Print `password`. Run it a few times with the same inputs and check
    the order changes each time.

**Extension:** replace steps 16â€“17 with one line:
`password = "".join(password_list)`.

*Adapted from: 100 Days of Code, Day 5.*
"""

import random


letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Easy version: add the requested characters in groups.
easy_password = ""
for _ in range(nr_letters):
    easy_password += random.choice(letters)
for _ in range(nr_symbols):
    easy_password += random.choice(symbols)
for _ in range(nr_numbers):
    easy_password += random.choice(numbers)

print("Easy password:", easy_password)

# Hard version: collect the characters, then shuffle them into a random order.
password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
hard_password = ""
for char in password_list:
    hard_password += char

print("Hard password:", hard_password)

# For real account passwords, use a cryptographically secure generator.

