from colorama import init
from termcolor import colored
import random
from replit import clear
from art import logo

init()
 
def guess_game():
  
  proceed = True
  while proceed == True:
    game = input("Do you want to play Guess The Number game? Type 'y' or 'n': ").lower()
    
    if game == 'y':
      clear()
      print(logo)
    else:
      proceed = False
      break
    
        
    print(colored('Welcome to Guess The Number Game!', 'blue'))
     
    print(colored('I am thinking of a number between 1 and 100.', 'white'))
    
    difficulty = input(f"Choose your difficulty. Type {colored('easy', 'light_cyan')} or {colored('hard', 'red')}: ").lower()
    
    
    attempt_h = 5
    attempt_e = 10
    
    guess =  random.randint(1, 100)
    
    if difficulty == 'easy':
      while attempt_e > 0:
        
        if attempt_e < 5:
          attempt_e_colored =  colored(attempt_e, 'red')
        elif attempt_e < 8:
          attempt_e_colored = colored(attempt_e, 'light_yellow')
        else:
          attempt_e_colored = colored(attempt_e, 'cyan')
          
        print(f"You have {attempt_e_colored} attempts to guess the number.")
        while True:
          
          try:
            number = int(input("Make a guess: "))
            if 1 <= number <= 100:
              break
            else:
              print("Please enter a number between 1 and 100.")
          except ValueError:
              print("Invalid input. Please enter a valid number.")
      
        if number == guess:
          print(f"You Got it. The number was {guess}.")
          break
      
        elif number > guess:
          attempt_e -= 1
          if attempt_e > 0:
            print("Too High!")
            print("Guess Again.")
          
        elif number < guess:
          attempt_e -= 1
          if attempt_e > 0:
            print("Too Low!")
            print("Guess Again.")
      
      else:
        print(f"You have run out of guesses. The number was {colored(guess, 'magenta')}.")
        guess_game()

    else:
      while attempt_h > 0:
        
        if attempt_h < 2:
          attempt_h_colored =  colored(attempt_h, 'red')
        elif attempt_h < 4:
          attempt_h_colored = colored(attempt_h, 'light_yellow')
        else:
          attempt_h_colored = colored(attempt_h, 'cyan')
          
        print(f"You have {attempt_h_colored} attempts to guess the number.")
        while True:
          
          try:
            number = int(input("Make a guess: "))
            if 1 <= number <= 100:
              break
            else:
              print("Please enter a number between 1 and 100.")
          except ValueError:
              print("Invalid input. Please enter a valid number.")
      
        if number == guess:
          print(f"You Got it. The number was {guess}.")
          break
      
        elif number > guess:
          attempt_h -= 1
          if attempt_h > 0:
            print("Too High!")
            print("Guess Again.")
          
        elif number < guess:
          attempt_h -= 1
          if attempt_h > 0:
            print("Too Low!")
            print("Guess Again.")
      
      else:
        print(f"You have run out of guesses. The number was {colored(guess, 'magenta')}.")
        guess_game()

guess_game()
        
      