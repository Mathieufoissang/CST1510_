"""Display a 10 by 10 multiplication table with aligned columns."""

for row in range(10):
    for column in range(10):
        print(f"{row * column:<4}", end="")
    print()
