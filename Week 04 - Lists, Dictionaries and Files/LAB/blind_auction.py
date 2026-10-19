"""Collect private bids and announce the highest bidder."""


bids = {}
keep_bidding = True

print("Welcome to the Blind Auction!")

while keep_bidding:
    name = input("What is your name? ").strip()
    bid = int(input("What is your bid? Â£"))

    # A later bid under the same name updates that dictionary entry.
    bids[name] = bid

    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no': "
    ).strip().lower()

    if other_bidders == "no":
        keep_bidding = False
    elif other_bidders == "yes":
        # This only clears the visible screen; it does not erase terminal history.
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

