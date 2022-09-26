#Step 1

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Rnaomly chooose a word from the word_list and assign it to a variable called chosen word.
import random
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#print(letter_guess)

#TODO-3 - Check if the letter the user guessed is one of the letter in the chosen_word
for char in chosen_word:
  if char == guess:
    print("Right")
  else:
    print("Wrong")