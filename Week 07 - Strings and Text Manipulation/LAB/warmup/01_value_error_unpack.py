# Fix: split only at the first equals sign.
piece = "note=server=east"
key, value = piece.split("=", 1)
print(key, value)
