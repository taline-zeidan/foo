
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
import os
import random
from blackjack_art import logo

def deal():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards) 

def calc_score(cards):
  """Take a list of cards and return the score cslculated from the cards."""
  if sum(cards)==21 and len(cards)==2 :
    return 0
  if 11 in cards and sum(cards)> 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play():
  print(logo)
  user = [deal(),deal()]
  computer = [deal(),deal()]
  game_over = False
  
  while not game_over:
    computer_score = calc_score(computer)
    user_score = calc_score(user)
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")
    if computer_score == 0 or user_score ==0 or user_score>21:
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
      if user_should_deal == 'y':
        user.append(deal())
      else:
        game_over =  True
        
  while computer_score !=0 and computer_score <17:
    computer.append(deal())
    computer_score = calc_score(computer)

def clear():
  # Check if the system is Windows
  if os.name == 'nt':
    os.system('cls')
  # For macOS and Linux
  else:
    os.system('clear')
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play()