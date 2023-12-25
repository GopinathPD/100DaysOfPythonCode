from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = []
bidding_continue = True

def add_bidders(name, bid):
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = bid
    bids.append(bidder)

def find_highest_bidder():
    highest_bid = 0
    highest_bidder = ""
    for bidder in bids:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            highest_bidder = bidder["name"]

    print(f"The winner is {highest_bidder} with a bid of 
${highest_bid}")

while bidding_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_bidders(name, bid)
    more_bidders = input("Are there any other bidders? Type 'yes' or 
'no'.\n")
    if more_bidders.lower() != "yes":
        find_highest_bidder()
        bidding_continue = False
    else:
        clear()
