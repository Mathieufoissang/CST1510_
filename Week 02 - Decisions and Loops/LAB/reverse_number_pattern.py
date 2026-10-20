"""Print a decreasing number pattern."""

for row in range(5, 0, -1):
    for number in range(row, 0, -1):
        print(number, end=" ")
    print()
