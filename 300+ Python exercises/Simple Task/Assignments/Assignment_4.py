try:
    marks = float(input("Enter your marks: "))
    if marks > 60:
        print("You can take addmission!")
    else:
        print(f"Sorry! You cannot take addmision, you need {60 - marks} more marks to take addmission")
except ValueError:
    print("Enter a valid number")