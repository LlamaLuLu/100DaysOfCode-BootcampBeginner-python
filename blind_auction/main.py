from replit import clear
from art import *

print(logo)
stop = False
bids = {}

def find_winner(biddings):
  highest_bid = 0
  winner = ""
  for bidder in biddings:
    amount = biddings[bidder]
    if amount > highest_bid:
      highest_bid = amount
      winner = bidder
  print(f"The winner is {winner} with a bid of R{amount}")

while not stop:
  name = input("What is your name? ")
  price = int(input("How much will you bid? R"))
  bids[name] = price

  cont = input("Are there any other users who would like to bid? ").lower()
  if cont == "no":
    stop = True
    find_winner(bids)
  elif cont == "yes":
    clear()