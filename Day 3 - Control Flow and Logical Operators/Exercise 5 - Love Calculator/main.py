# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
conbined_names = (name1+name2).lower()

true_count = conbined_names.count('t') + conbined_names.count('r') + conbined_names.count('u') + conbined_names.count('e')
love_count = conbined_names.count('l') + conbined_names.count('o') + conbined_names.count('v') + conbined_names.count('e')

total_count = f"{true_count}{love_count}"

if int(total_count) < 10 or int(total_count) > 90:
  print("Your score is "+total_count+", you go together like coke and mentos.")
elif int(total_count) >= 40 and int(total_count) <= 50:
  print("Your score is "+total_count+", you are alright together.")
else:
  print("Your score is "+total_count+".")
