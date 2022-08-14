import random

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
print("Let's play a game of rock-paper-scrissors")
user_pick = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors"))
list = ["rock","paper","scissors"]
computer_pick = list[random.randint(0,len(list)-1)]

if user_pick == 0 and computer_pick == "scissors":
  print(rock)
  print("Computer choose:")
  print(scissors)
  print("You won")
elif user_pick == 1 and computer_pick == "rock":
  print(paper)
  print("Computer choose:")
  print(rock)
  print("You won")
elif user_pick == 2 and computer_pick == "paper":
  print(scissors)
  print("Computer choose:")
  print(paper)
  print("You won")
elif user_pick == 0 and computer_pick =="paper":
  print(rock)
  print("Computer choose:")
  print(paper)
  print("You lose")
elif user_pick == 1 and computer_pick == "scissors":
  print(paper)
  print("Computer choose:")
  print(scissors)
  print("You lose")
elif user_pick == 2 and computer_pick == "rock":
  print(scissors)
  print("Computer choose:")
  print(rock)
  print("You lose")
else:
  print("It's a draw")

