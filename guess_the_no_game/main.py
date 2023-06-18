from replit import clear
from art import logo
from random import *

EASY_LVL_TURNS = 10
HARD_LVL_TURNS = 5
  
def difficulty_setting():  
  level = input("Choose your difficulty: 'easy' or 'hard' ")
  if level == "easy" or level == "e" or level == "E":
      return EASY_LVL_TURNS
  else:
    return HARD_LVL_TURNS
        
def compare_number(guess, chosen_number, turns):
  if guess > chosen_number:
    guess = print("\nToo high.")
    return turns - 1
  elif guess < chosen_number:
    guess = print("\nToo low.")
    return turns - 1
  else:
    print(f"\nYou got it! The number was {chosen_number}. YOU WIN!🥳")
    print("\nGAME OVER")

def run_game(turns, chosen_number):
  clear()
  print(f"Psst, let me give you a big hint... The number might be {chosen_number}, but not even I know the truth...")
  guess = 0
  while guess != chosen_number:
    print(f"You have {turns} attempts to guess the number.")
    guess = int(input("What\'s your guess: "))
    
    turns = compare_number(guess, chosen_number, turns)
    if turns == 0:
      print(f"\nYou\'ve run out of all your attempts! The number was {chosen_number}. Better luck next time.")
      return
    elif guess != chosen_number:
      print("Guess again. ")



print(logo)
print("Welcome to Guess the Number! You\'re up for a treat!\nI\'m thinking of a number between 1 and 100. Can you guess the one I\'m thinking of? ")
turns = 0
level = "_"
chosen_number = randint(1, 100)

turns = difficulty_setting()
run_game(turns, chosen_number)