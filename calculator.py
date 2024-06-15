#used this to test recursion, while loops that dont run infinitely,
#as well as a dictionary. 
from calculator_art import logo
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {"+": add, 
              "-": subtract, 
              "*": multiply, 
              "/": divide}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?:"))
  for symbol in operations:
    print(symbol, end=" ")
  print()
  
  should_continue =  True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?:"))
    function = operations[operation_symbol]
    answer = function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower() == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()
  
calculator()
