#Number Guessing Game

from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")


def level_difficulty():
  user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if user_difficulty == 'hard':
    return HARD_LEVEL_TURNS
  else:
    return EASY_LEVEL_TURNS
  

def number_guessing():
  random_number = random.randint(1,100)
  lives = level_difficulty()
  print(f"You have {lives} attemps remaining to guess the number.")
  end_of_game = False
  while not end_of_game:
    number_to_guess = int(input("Make a guess:  "))
    if lives > 1:
      if number_to_guess == random_number:
        end_of_game = True
        print(f"You guessed the right number: {random_number}")
      elif number_to_guess > random_number:
        lives-=1
        print("Too high.")
        print("Guess again.")
        print(f"You have {lives} attemps remaining to guess the number.")
      elif number_to_guess < random_number:
        lives-=1
        print("Too low.")
        print("Guess again.")
        print(f"You have {lives} attemps remaining to guess the number.")
    else:
      end_of_game=True
      print(f"You've run out of guesses, you lose. The number was: {random_number}")

number_guessing()  
    
  