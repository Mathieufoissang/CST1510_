"""Calculate the sum of the integers from 1 through n."""

n = int(input("Enter a positive integer n: "))
total = n * (n + 1) // 2

print(f"Sum of 1..{n} = {total}")
