import os

print("*************Welcome to Silent Auction program************")
def finding_winning_bidder(bidder_details):
    highest_bid = 0
    winner = 0
    for bidder in bidder_details:
        bidder_price = bidder_details[bidder]
        if bidder_price > highest_bid:
            highest_bid = bidder_price
            winner = bidder
    print(f"here is the list of bidders {bidder_details}")
    print(f"the is {winner} with a bid price {highest_bid}")

bidder_data = {}
end_of_Bidding = False
while not end_of_Bidding:
    user_name = input("Enter the user name :")
    bid = int(input("Enter the bid value :"))
    bidder_data[user_name] = bid
    more_bidder = input("Are there more bidder Type yes or no").strip().lower()
    print (f"you selected {more_bidder}")
    if more_bidder=='no':
        end_of_Bidding=True
        finding_winning_bidder(bidder_data)
    elif more_bidder=='yes':
        os.system('cls')






