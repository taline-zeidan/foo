from gavel_art import gavel
import os

keep_bidding = True
bids = {}

def find_highest_bidder(bids):
  max_bid = 0
  highest_bidder = ""
  #assuming no two will bid the same which is kind of dumb, I admit, but cut me some slack..
  for bidder in bids:
    if bids[bidder] > max_bid:
      max_bid = bids[bidder]
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of ${max_bid}")
      
#copied this from chatGPT cz the one angela uses only works in replit lol
def clear():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
while keep_bidding:
  print(gavel)
  #also naively assuming they will not input weird text instead of bid and run into an error
  bidder =  input("What is your name? ")
  bid =  int(input("What is your bid? $"))
  if bidder not in bids:
    bids[bidder]=bid
  else:
    print(f"{bidder}, you already bid once!")
  continue_bid = ""
  while continue_bid != 'yes' and continue_bid != 'no':
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.")
    if continue_bid == "no":
      keep_bidding = False
      find_highest_bidder(bids)
    elif continue_bid == "yes":
      clear()
  
    
    



