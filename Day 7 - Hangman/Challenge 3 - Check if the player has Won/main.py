#Step 3
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in chosen_word:
  display.append("_")
  
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
while not end_of_game:
  user_input = input("Pick a letter: ").lower()
  #Check guessed letter
  for i in range(word_length):
    if(chosen_word[i]==user_input):
      display[i]=user_input
  print(display)
  #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
  #First solution
  # white_spaces = 0
  # for char in display:
  #   if(char=="_"):
  #     white_spaces+=1
  # if(white_spaces==0):
  #   end_of_game = True
  #   print("You won")
  #Second solution
  if "_" not in display:
    end_of_game = True
    print("You won")
