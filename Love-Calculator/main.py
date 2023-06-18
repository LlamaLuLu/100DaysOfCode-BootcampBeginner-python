# 7/11/2021
# calculates romantic compatibility score of couple based on letters of name

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
true_love = name1 + name2

true_count = str(true_love.count("t") + true_love.count("r") + true_love.count("u") + true_love.count("e"))
love_count = str(true_love.count("l") + true_love.count("o") + true_love.count("v") + true_love.count("e"))
love_score = int(true_count + love_count)

if love_score < 10 or love_score >= 90:
  print(f"your score is {love_score}, you go together like coke and mentos.")
elif love_score >40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
