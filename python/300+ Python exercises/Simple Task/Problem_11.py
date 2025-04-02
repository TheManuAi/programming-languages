try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 > num2:
        print(f"{num1} is greater than the {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than the {num1}")
    else:
        print("They both are equal")
except ValueError:
    print("Enter a valid number!")