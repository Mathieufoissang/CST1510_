"""Generate passwords from a requested number of characters."""

import random


letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

easy_password = ""
for _ in range(nr_letters):
    easy_password += random.choice(letters)
for _ in range(nr_symbols):
    easy_password += random.choice(symbols)
for _ in range(nr_numbers):
    easy_password += random.choice(numbers)

print("Easy password:", easy_password)


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


