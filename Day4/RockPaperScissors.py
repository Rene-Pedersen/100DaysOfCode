import random
import time

random.seed(time.time_ns())

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
print("Lets play Rock, Paper, Scissors.")
u_guess = int(input("What is your selection? 0 for Rock, 1 for Paper and 2 for Scissors\n"))
c_guess = random.randint(0, 2)

options = [rock, paper, scissors]

print(options[u_guess])
print("Computer chose:")
print(options[c_guess])

if u_guess == c_guess:
    print("It's a draw")
elif (u_guess == 0 and c_guess == 2) or (u_guess == 1 and c_guess == 0) or (u_guess == 2 and c_guess == 1):
    print("You win!")
else:
    print("You Lose")
