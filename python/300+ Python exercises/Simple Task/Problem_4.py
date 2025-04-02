try:
    age = float(input("Enter your age: "))
    if age > 18:
        print("You can participate in voting!")
    else:
        print(f"Sorry! You cannot participate in voting, you will be able to participate after {18 - age} year(s)")
except ValueError:
    print("Enter a valid number")