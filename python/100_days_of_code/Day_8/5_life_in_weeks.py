def life_in_weeks(age):
    x = (90 - age) * 52
    print(f"You have {x} weeks left if you live until 90 years old.")
    
life_in_weeks(int(input("What is your current age: ")))