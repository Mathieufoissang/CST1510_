"""""
Banker Roulette

**Uses:** lists, `random.choice()`, `random.randint()`, `len()`

1. At the top of your file, write `import random`.
2. Create a variable called `friends` and set it to a list of names,
   for example `["Alice", "Bob", "Charlie", "Dana", "Ella"]`.

**Version 1 — `random.choice()`**

3. Call `random.choice(friends)` and store the result in a variable
   called `payer`.
4. Print `payer` along with a message, for example
   `f"{payer} is paying the bill today!"`.

**Version 2 — `random.randint()` and an index**

5. Use `len(friends)` to get the number of names and store it in
   `num_friends`.
6. Create a variable `index` and set it to
   `random.randint(0, num_friends - 1)`.
   (Lists start at index `0`, so the last valid index is one less than
   the length.)
7. Use the index to pick a name from the list: `payer = friends[index]`.
8. Print `payer` with the same message as before.
9. Run both versions a few times and check that a different name can
   come up each time."""""

import random


friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]

payer = random.choice(friends)
print(f"{payer} is paying the bill today! (random.choice)")

num_friends = len(friends)
index = random.randint(0, num_friends - 1)
payer = friends[index]
print(f"{payer} is paying the bill today! (random.randint)")
