"""Choose a friend at random to pay the bill."""

import random


friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]

# Version 1: random.choice() selects an item directly from the list.
payer = random.choice(friends)
print(f"{payer} is paying the bill today! (random.choice)")

# Version 2: choose a valid list index, then use it to select a friend.
num_friends = len(friends)
index = random.randint(0, num_friends - 1)
payer = friends[index]
print(f"{payer} is paying the bill today! (random.randint)")
