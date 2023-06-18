# 15/11/2021
# hangman game

import random
from hangman_art import *
import hangman_words as dictionary
from replit import clear

chosen_word = random.choice(dictionary.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for blank in range(word_length):
    star = chosen_word[blank]
    if any(['a' == star, 'e' == star, 'i' == star, 'o' == star, 'u' == star]):
        display.insert(blank, "*")
    else:
      display.insert(blank, "_")
print(display)

# for _ in range(word_length):
#     display += "_"

guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in guessed_letters:
      print(f"You have already guessed '{guess}'. Try something else.")
    guessed_letters.append(guess)
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose 1 life.")
        lives -= 1
        
    print(f"{' '.join(display)}")
    print(stages[lives])
    print(f"Lives left: {lives}")

    if lives == 0:
        end_of_game = True
        print("You LOSE! Don't be too nervous, just try again :)")
        print(game_over[2])

    if "_" not in display:
        if lives == 5 or lives == 6:
          end_of_game = True
          print("Did you cheat bruh??! Remember, Jesus is watching you...")
          print(game_over[0])
        else:
          end_of_game = True
          print("You WIN!!! Nice one!")
          print(game_over[1])
