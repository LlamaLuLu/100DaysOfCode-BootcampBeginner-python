# 14/2/2023

############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
# from replit import clear
from art import logo


def deal_card():
  """returns random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """returns sum of cards in deck"""
  
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  else:
    return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "\nIt's a DRAW!🙌"
  elif computer_score == 0:
    return "\nYou just LOST!🫣 Your opponent got a blackjack."
  elif user_score > 21:
    return "\nYou went over 21 and LOST!🫣"
  elif user_score == 0:
    return "\nYOU WIN with a blackjack!!!🤩🤩🤩"
  elif computer_score > 21:
    return "\nYOU WIN!!!🤩🤩🤩 Your opponent went over 21!"
  elif user_score > computer_score:
    return"\nYOU WIN!!!🤩🤩🤩 You were way closer to 21"
  else:
    return "\nYou just LOST!🫣 Too far off."
  
def play_game():
  print(logo)
  
  game_over = False
  user_cards = []
  computer_cards = []
  for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"\nYour cards are {user_cards}. Current score: {user_score}.")
    print(f"The computer's 1st card is {computer_cards[0]}.")
      
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      progress = input("\nDo you want to draw another card?\n'y' or 'n' ")
      if progress == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
      else:
        game_over = True

    while computer_score < 17 and computer_score != 0:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

  print(f"\n  Your final hand was {user_cards}. Final score: {user_score}.")
  print(f"  The computer's final hand was {computer_cards}. Final score: {computer_score}.")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

  
while input("Do you want to play a game of blackjack? 'y' or 'n' ") == "y":
  # clear()
  play_game()
print("\nThanks for passing by. Have a good day!🫶")

