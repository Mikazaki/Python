from art import logo
import os

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calculator():
  print(logo)
  operation = {"+": add, "-": subtract, "*": multiply, "/": divide}
  
  num1 = float(input("What is the first number: "))
  num2 = float(input("What is the second number: "))
  
  
  for key in operation:
    print(key)
  
  symbol = input("Pick an operation for the line above: ")
  
  answer = operation[symbol](num1, num2)
  
  print(f"{num1} {symbol} {num2} = {answer}")
  
  question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to to start a new calculation: ").lower()
  
  while question == "y":
    operation = {"+": add, "-": subtract, "*": multiply, "/": divide}
  
    num1 = answer
    num2 = float(input("What is the next number: "))
    
    
    for key in operation:
      print(key)
    
    symbol = input("Pick an operation for the line above: ")
    
    answer = operation[symbol](num1, num2)
    
    print(f"{num1} {symbol} {num2} = {answer}")
    
    question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

  if question == "n":
    cls()
    calculator()
  
calculator()
