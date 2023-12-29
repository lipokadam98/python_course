import os

import bidding_art

bids = []


def check_highest_bidder():
    highest_bidders = []
    highest_bid = 0
    for bid in bids:
        current_bid = int(bid['bid'])
        if current_bid > highest_bid:
            highest_bid = current_bid
            highest_bidders = [bid['name']]
        elif current_bid == highest_bid:
            highest_bidders.append(bid['name'])

    if len(highest_bidders) == 1:
        print('The winner is ' + highest_bidders[0] + " with a bid of $" + str(highest_bid) + ".")
    else:
        print('There is a tie between the following bidders with a bid of $' + str(highest_bid) + ":")
        for bidder in highest_bidders:
            print("- " + bidder)


def add_new_bid():
    name = input('What is your name?: ')
    bid = input("What's your bid?: $")

    new_bid = {
        "name": name,
        "bid": bid
    }
    bids.append(new_bid)
    other_bidder = input('Are there any other bidders? Type "yes" or "no" ')
    if other_bidder == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        add_new_bid()
    elif other_bidder == 'no':
        os.system('cls' if os.name == 'nt' else 'clear')
        check_highest_bidder()


print(bidding_art.logo)
print('Welcome to the secret auction program.')

add_new_bid()
