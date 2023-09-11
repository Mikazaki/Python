from colorama import init
from termcolor import colored
import random
from art import logo, vs
from game_data import data
import os
init()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def highlow():
  print(logo)
  proceed = True
  score = 0
  new = None
  while proceed == True:
    
    def new_score(correct_answer, score):
      if correct_answer:
        score += 1
      return score
      
    if new is None:
      generate = random.sample(data, k=2)
      a = generate[0]
      b = generate[1]
    else:
      print(f"You are Correct! Current score: {colored(score,'green')}")
      while True:
        generate = random.choice(data)
        if generate != a and generate != b:
            b = generate
            break
      a = new
    
    
    
    comp_a = f"{a['name']}, {a['description']}, from {a['country']}"
    comp_b = f"{b['name']}, {b['description']}, from {b['country']}"
      
    print(f"Compare A: {comp_a}.\n")

    print(vs)
    
    print(f"\nAgainst B: {comp_b}.")
  
    fol_a = a["follower_count"]
    fol_b = b['follower_count']
    
    
    who = input(f"Who has more followers? Type {colored('A','blue','on_black', ['bold'])} or {colored('B','light_magenta','on_black', ['bold'])}: ").lower()

    if (who == "a" and fol_a > fol_b) or (who == "b" and fol_b > fol_a):
      score = new_score(True, score)
      cls()
      print(logo)
      if who == "a":
        new = a
      else:
        new = b
        

    else:
      cls()
      print(f"Sorry that is wrong. Final score: {score}")
      play = input(f"Do you want to play again? Type {colored('Y',color='blue',attrs=['bold'])} or {colored('N',color='red',attrs=['bold'])}: ").lower()
      if play == "y":
        cls()
        highlow()
      else:
        break
      
highlow()
    




