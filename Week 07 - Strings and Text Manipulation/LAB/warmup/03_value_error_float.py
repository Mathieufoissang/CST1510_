# Fix: report values that cannot be converted instead of crashing.
raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)
for piece in rest.split(","):
    key, value = piece.split("=", 1)
    try:
        number = float(value.strip())
    except ValueError:
        print(f"Could not convert {key.strip()}: {value.strip()}")
    else:
        print(key.strip(), number)
