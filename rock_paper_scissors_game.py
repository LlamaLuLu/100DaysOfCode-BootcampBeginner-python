# 8/11/2021

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

#            0     1       2
options = [rock, paper, scissors]

user_hand = int(input("What do you choose? Type 1 for ROCK, 2 for PAPER or 3 for SCISSORS, the tap ENTER.\n"))

if user_hand > 3 or user_hand < 0:
  print("\nYou typed an invalid number. Try again.")  

else:
  print("\nYour hand:")
  print(options[user_hand - 1])

  print("\nComputer's hand:")
  comp_hand = random.randint(0, 2)
  print(options[comp_hand])

  if comp_hand == user_hand:
    print("DRAW \nSo close! Tap run to try again.")
    print("""
            ,,,,,,,, ,,,,,,,
         '.-''''''''''''-.'
        ''                ''
        ''                ''
        ''  '``'    '``'  ''
        ''  .--.    .--.  ''
        '' '(_).'  '(_).' ''
        ''      '  '      ''
        ''      '  '      ''
        ''      '  '      ''
        ''    .-'  '-.    ''
        ''`   '-'--'-'   ,''
        '''`  .--.--.   ,'''
        ''''`  `---'   ,''''
        '''''`        ,'''''
        ''''''`......,''''''
        '`'''''       ''''''
luser
    """)
  
  elif (comp_hand < user_hand) or (comp_hand == 2 and user_hand == 0):
    print("WIN \nWell done! Give yourself a pat on the back :)")
    print("""
               ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
    """)

  elif (comp_hand > user_hand) or (comp_hand == 0 and user_hand == 2):
    print("LOSE \nHaha! Why don't you try again?")
    print(r"""
                    __.-=-._
                ,""\_    _/"'\
               -__o.-'  '-._0/
             _ |    .'  \    \  _
            ( \|  / |  | `   (_/ )
             )/  / /   \\_     ,(
             \|(___    ___) .(\_/
             /     \'_|       \
             \-'''.____.''''--/
              `.-.__,__.__.-'/
                `-._______.-'
                       _\ \__
                     /_  \'_ \-.
                    |/ \ /  \/     
                        /o          
    """)
  
  
