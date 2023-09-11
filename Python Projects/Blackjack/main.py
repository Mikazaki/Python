from art import logo
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def blackjack():
  print(logo)
  proceed = True
  while proceed == True:
    
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    if game == 'y':
      cls()
      print(logo)
    else:
      proceed = False
      break
      blackjack()
    
    you = random.choices(cards, k=2)
    comp = random.choices(cards, k=2)

    
  
    def your_score():
      total = 0
      for card in you:
        total += card
        if total == 21:
          total = 0
      for card in you:
        if card == 11 and total > 21:
          you[you.index(11)] = 1
          total -= 10
      return total    
    
    def comp_score():
      total_t = 0
      for card in comp:
        total_t += card
        if total_t == 21:
          total_t = 0
      for card in comp:
        if card == 11 and total_t > 21:
          comp[comp.index(11)] = 1
          total_t -= 10
      return total_t    
        
    
    print(f"  Your Cards: {you}, current score: {your_score()}")
    print(f"  Computer's First Hand: {comp[0]}")

    next = input("Type 'y' to take another card or 'n' to pass: ").lower()

    while next == 'y':
        you.append(random.choice(cards))
        comp.append(random.choice(cards))
        print(f"  Your Cards: {you}, current score: {your_score()}")
        print(f"  Computer's First Hand: {comp[0]}")
        
  
        if your_score() and comp_score() == 0 or your_score() == comp_score():
          print(f"  Your Final Hand: {you}, final score: {your_score()}")
          print(f"  Computer's Final Hand: {comp}, final score: {comp_score()}")
          print("Draw")
          break
      
        elif your_score() > 21 and comp_score() < 21:
          print(f"  Your Final Hand: {you}, final score: {your_score()}")
          print(f"  Computer's Final Hand: {comp}, final score: {comp_score()}")
          print("Busted. You Lose")
          break

        elif your_score() < 21 and comp_score() > 21:
          print(f"  Your Final Hand: {you}, final score: {your_score()}")
          print(f"  Computer's Final Hand: {comp}, final score: {comp_score()}")
          print("You Win")
          break
        
        else:
          next = input("Type 'y' to take another card or 'n' to pass: ").lower()
       
      
  
    else:
      print(f"  Your Final Hand: {you}, final score: {your_score()}")
      print(f"  Computer's Final Hand: {comp}, final score: {comp_score()}")
    
      if your_score() == 0 or comp_score() == 0:
        print("Win with a Blackjack")
      
      elif your_score() < comp_score():
        print("You Lose")
      
      else:
        print("You Win")
    
      
  
      
      

         
blackjack()


  

  



