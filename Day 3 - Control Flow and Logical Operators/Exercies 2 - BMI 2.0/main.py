# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_calculator = round(weight/height**2)


if bmi_calculator <= 18.5:
    print(f"Your BMI is {bmi_calculator}, you are underweight.")
elif bmi_calculator > 18.5 and bmi_calculator < 25:
    print(f"Your BMI is {bmi_calculator}, you have a normal weight.")
elif bmi_calculator > 25 and bmi_calculator < 30:
    print(f"Your BMI is {bmi_calculator}, you are slightly overweight.")
elif bmi_calculator > 30 and bmi_calculator < 35:
    print(f"Your BMI is {bmi_calculator}, you are obese.")
else:
    print(f"Your BMI is {bmi_calculator}, you are clinically obese.")