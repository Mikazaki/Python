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

import random

game = int(input("Make your choice. Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

rpc = [rock, paper, scissors]

print(rpc[game])

computer = random.randint(0, 2)

if computer == 0:
  print(f"The computer chose:\n {rpc[computer]}")
elif computer == 1:
  print(f"The computer chose:\n {rpc[computer]}")
elif computer == 2:
  print(f"The computer chose:\n {rpc[computer]}")

if game == computer:
  print("It is a draw!")
elif game == 0 and computer == 2 or game == 1 and computer == 0 or game == 2 and computer == 1:
  print("Player Wins")
else:
  print("Bot Wins BOZO")

