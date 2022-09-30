#Calculator
from art import logo
from replit import clear
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  clear()
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  end_of_game = False
  while not end_of_game:
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit press, or start a fresh calculator type 'start'")
    if keep_going == 'n':
      end_of_game = True
    elif keep_going == 'y':
      num1 = answer
    elif keep_going == 'start':
      calculator()
    else:
      print("Wrong input, exiting the calculator")
      end_of_game = True

calculator()