"""## Blind Auction

**Uses:** dictionaries, `while` loops, looping over `.items()`

1. Create a variable called `bids` and set it to an empty dictionary
   `{}`.
2. Create a variable `keep_bidding` and set it to `True`.
3. Start a `while keep_bidding:` loop.
4. Inside the loop, use `input()` to ask for the bidder's name and store
   it in `name`.
5. Ask for their bid, convert it with `int()`, and store it in `bid`.
6. Add the pair to the dictionary: `bids[name] = bid`.
7. Ask: `"Are there any other bidders? Type 'yes' or 'no':"` and store
   the answer in `other_bidders`.
8. If `other_bidders == "no"`, set `keep_bidding = False`.
9. If they typed `"yes"`, print `"\n" * 100` to push the previous bid off
   the screen, so the next bidder can't see it.
10. Outside the loop, create a variable `highest_bid` and set it to `0`.
11. Create a variable `winner` and set it to `""`.
12. Write a loop: `for name, bid in bids.items():`
13. Inside the loop, use an `if` to check whether `bid > highest_bid`.
    If it is:
    - set `highest_bid = bid`
    - set `winner = name`
14. After the loop, print the winner and their bid, for example
    `f"The winner is {winner} with a bid of £{highest_bid}."`
    Never print anyone else's bid — that's the point of a *blind*
    auction."""


bids = {}
keep_bidding = True

print("Welcome to the Blind Auction!")

while keep_bidding:
    name = input("What is your name? ").strip()
    bid = int(input("What is your bid? Â£"))

    bids[name] = bid

    other_bidders = input(

    ).strip().lower()

    if other_bidders == "no":
        keep_bidding = False
    elif other_bidders == "yes":
        
        print("\n" * 100)
    else:
        print("Please answer 'yes' or 'no'.")

highest_bid = 0
winner = ""

for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

if winner:
    print(f"The winner is {winner} with a bid of Â£{highest_bid}.")
else:
    print("No bids were entered.")

