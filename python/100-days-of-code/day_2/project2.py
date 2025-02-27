print("Welcome to the tip calculator!")
bill = float(input("What was the total bill: "))
tip = int(input("What percentage tip would you like to give:  "))
people = int(input("How many people to split the bill: "))

tip_percentage = (tip / 100) * bill
total_bill = bill + tip_percentage
split = total_bill / people

print(f"Each person should pay: {round(split, 2)}")

