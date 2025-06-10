def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

auction = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid price: "))
    auction[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bid(auction)
    elif should_continue == "yes":
        print("\n" * 28)

