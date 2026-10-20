"""Collect three configuration entries and print an INI-style block."""

first_key = input("First key: ")
first_value = input("First value: ")
second_key = input("Second key: ")
second_value = input("Second value: ")
third_key = input("Third key: ")
third_value = input("Third value: ")

print("[config]")
print(f"\t{first_key} = {first_value}")
print(f"\t{second_key} = {second_value}")
print(f"\t{third_key} = {third_value}")
