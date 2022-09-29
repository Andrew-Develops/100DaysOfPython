from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

#Solution 1

bidding_war = {}
def auction_house():
  end_game = False
  while not end_game:
    count = 0
    returned_key = ""
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidding_war[name]=bid
    other_bidders = input("Are there are other bidders? Type 'yes or 'no' \n")
    if other_bidders == "no":
      for key in bidding_war:
        if count < bidding_war[key]:
          count = bidding_war[key]
          returned_key = key
      print(f"The winner is {returned_key} with a bid of {count}$")
      end_game = True
    else:
      clear()
      
auction_house()

#Solution 2

bids = {}
bidding_finished = False

def auction_house_solutio2():
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
