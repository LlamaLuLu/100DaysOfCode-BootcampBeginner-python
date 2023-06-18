# 6/11/2021
# calculates amount each person at table must pay for bill

print("Welcome to the tip calculator!")
bill = float(input("What was the total BILL?  "))
tip = int(input("How much TIP would you like to give?  "))

#takes any string & makes lowercase
sharing_prompt = input("Are you splitting the bill?  ").lower()

#bill + tip
if sharing_prompt == "no":
  total_bill = bill * (1 + tip / 100) 
  final_amount = "{:.2f}".format(round(total_bill))
  print(f"You should pay: R{final_amount}")
#total / ppl
elif sharing_prompt == "yes":
  ppl = int(input("Between how many people?  "))
  total_bill = bill * (1 + tip / 100)
  amount_shared = round(total_bill / ppl, 2)
  final_amount = "{:.2f}".format(amount_shared)
  print(f"Each person should pay: R{final_amount}")

else:
  print("There was an incorrect input. Please try again.")
