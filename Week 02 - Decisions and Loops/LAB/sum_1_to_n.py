"""Add all integers from 1 through n."""

n = int(input("Enter the value n: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = 0
    for number in range(1, n + 1):
        total += number
    print(f"The sum of all numbers until {n} is {total}")
