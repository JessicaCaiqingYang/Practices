import random

def dice_roll(number):
  count = { 
    2: 0, 
    3: 0, 
    4: 0, 
    5: 0, 
    6: 0, 
    7: 0, 
    8: 0, 
    9: 0,
    10: 0,
    11: 0,
    12: 0
    }
  for each_roll in range(number):
    dice_1 = random.randint(1, 6) 
    dice_2 = random.randint(1, 6) 
    a_roll = dice_1 + dice_2
    count[a_roll] += 1 
  return count

user_guess = int(input("You have two dices to roll. Enter the number you are trying to get: "))

def dice_roll_probablity(number):
  if user_guess < 2 or user_guess > 12:
    return f"The chance of you getting {user_guess} is 0%" 
  else:
    count = dice_roll(number)
    outcome = count[user_guess] / number * 100
    return f"The chance of you getting {user_guess} is {int(outcome)}%"

print(dice_roll_probablity(100))
