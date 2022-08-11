print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
first_input = input("Type 'left' or 'right'\n").lower()

if first_input == "left":
  print("You came to a lake. There is an island.")
  second_input = input("Type 'wait' to wait for a boat. Type 'swim' toswim across\n").lower()
  if second_input == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    third_input = input("Pick a color. 'red', 'blue' or 'yellow'\n").lower()
    if third_input == 'red':
      print("Burned by fire. Game over!")
    elif third_input == 'yellow':
      print("You Win!")
    elif third_input == 'blue':
      print("Eaten by beasts. Game over!")
    else:
      print("Game over")
  else:
    print("You were attacked by trout. Game over!")
else:
  print("You felt into a hole. Game over!")







