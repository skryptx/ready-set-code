from utilities.clear_console import clear

bids = {}
print("Welcome to the secret auction program")
continue_bid = "yes"

while continue_bid == "yes":
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bids[name] = bid_amount

    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

max_bid = 0
max_bid_person = ""

for key in bids:
    if bids[key] >= max_bid:
        max_bid = bids[key]
        max_bid_person = key

print(f"The winner is {max_bid_person} with a bid of ${max_bid}")