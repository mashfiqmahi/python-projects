from art import logo
from higesht_bidder import higesh_bid_finder

print(logo)
bids = {}
finished_bid = False
while not finished_bid:
    name = input("What's your name? ")
    bid = int(input("What's your bidding amount? $"))
    bids[name] = bid
    should_continue = input('Is there any other bidder? type "yes or "no\n')
    if should_continue == 'no':
        finished_bid = True
        higesh_bid_finder(bids)

