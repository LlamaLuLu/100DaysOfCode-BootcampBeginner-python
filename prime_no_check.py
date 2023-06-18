# 15/11/2021

def prime_checker(number):
  factors = 0
  for n in range(1, number + 1):
    if number % n == 0:
      factors += 1
  if factors == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

    
n = int(input("Check this number: "))
prime_checker(number=n)
