# 15/2/2023
# higher-lower game: choose which celeb/group has more followers on instagram

import random
from art import *
from game_data import data
import os


game_over = False
new_data = data

def new_entry():
  entry = random.choice(new_data)
  new_data.remove(entry)
  return entry


person1 = new_entry()
person2 = new_entry()
choices = [person1, person2]
score = 0
print(logo)

while game_over == False:
  print()
  print(f"Compare A: '{choices[0]['name']}', a {choices[0]['description']} from {choices[0]['country']}.")
  print(f"{vs}\n")
  print(f"Compare B: '{choices[1]['name']}', a {choices[1]['description']} from {choices[1]['country']}.\n")

  answer = input("Who has more followers? Type 'A' or 'B': ")

  if answer == ('A' or 'a'):
    c = 0
    oc = 1
  else:
    c = 1
    oc = 0
    
  if choices[c]['follower_count'] > choices[oc]['follower_count']:
    os.system('clear')
    print(logo)
    score += 1
    print(f"\nYou're right! Current score: {score}.")
  else:
    os.system('clear')
    print(f"\nSorry, that's wrong. Final score: {score}.")
    game_over = True
  
  choices[0] = choices[1]
  choices[1] = new_entry()
  
  
