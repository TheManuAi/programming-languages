try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operation ( +, -, *, / ): ").strip()
    num2 = float(input("Enter the second number: "))
    if operator == "/" and num2 == 0:
        print("Division with 0 is not defined")
    elif operator == "/":
        print(f"The result is {num1/num2}")
    elif operator == "+":
        print(f"The result is {num1+num2}")
    elif operator == "-":
        print(f"The result is {num1-num2}")
    elif operator == "*":
        print(f"The result is {num1*num2}")
    else:
        print("Enter a valid operation")
except ValueError:
    print("Enter valid input(s)")