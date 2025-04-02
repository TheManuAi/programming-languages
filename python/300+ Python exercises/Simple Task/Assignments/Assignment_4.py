try:
    marks = float(input("Enter your marks: "))
    if marks > 60:
        print("You can take admission!")
    else:
        print(f"Sorry! You cannot take admission, you need {60 - marks} more marks to take admission")
except ValueError:
    print("Enter a valid number")