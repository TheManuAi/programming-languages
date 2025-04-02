try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operation ( +, -, *, / ): ").strip()
    num2 = float(input("Enter the second number: "))
    operator2 = input("Enter the operation(+, -, *, /):").strip()
    num3 = float(input("Enter the third number: "))

    if operator == "/" and num2 == 0:
        print("Division with 0 is not defined")
    elif operator2 == "/" and num3 == 0:
        print("Division with 0 is not defined")
        
    elif operator == "/" and operator2 == "/":
        print(f"The result is {(num1/num2)/num3}")
    elif operator == "/" and operator2 == "*":
        print(f"The result is {(num1/num2)*num3}")
    elif operator == "/" and operator2 == "+":
        print(f"The result is {(num1/num2)+num3}")
    elif operator == "/" and operator2 == "-":
        print(f"The result is {(num1/num2)-num3}")

    elif operator == "*" and operator2 == "/":
        print(f"The result is {(num1*num2)/num3}")
    elif operator == "*" and operator2 == "*":
        print(f"The result is {(num1*num2)*num3}")
    elif operator == "*" and operator2 == "+":
        print(f"The result is {(num1*num2)+num3}")
    elif operator == "*" and operator2 == "-":
        print(f"The result is {(num1*num2)-num3}")

    elif operator == "+" and operator2 == "/":
        print(f"The result is {(num1+num2)/num3}")
    elif operator == "+" and operator2 == "*":
        print(f"The result is {(num1+num2)*num3}")
    elif operator == "+" and operator2 == "+":
        print(f"The result is {(num1+num2)+num3}")
    elif operator == "+" and operator2 == "-":
        print(f"The result is {(num1+num2)-num3}")

    elif operator == "-" and operator2 == "/":
        print(f"The result is {(num1-num2)/num3}")
    elif operator == "-" and operator2 == "*":
        print(f"The result is {(num1-num2)*num3}")
    elif operator == "-" and operator2 == "+":
        print(f"The result is {(num1-num2)+num3}")
    elif operator == "-" and operator2 == "-":
        print(f"The result is {(num1-num2)-num3}")

    else:
        print("Enter a valid operation")
except ValueError:
    print("Enter valid input(s)")