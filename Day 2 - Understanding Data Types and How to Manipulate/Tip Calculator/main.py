print("Welcome to the tip calculator")
total_bill = float(input("What was that total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
number_of_person = int(input("How many mepople to split the bill?\n"))
total_tip = total_bill + total_bill * (tip_percentage/100)
to_pay =round(float(total_tip / number_of_person),2)

print(f"Each person should pay: ${to_pay}")
