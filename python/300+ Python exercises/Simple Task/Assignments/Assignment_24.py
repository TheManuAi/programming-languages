def calculate(n1, op, n2):
    if op == "/" and n2 == 0:
        print("Division with 0 is not defined")
    elif op == "/":
        print(f"The result is {n1/n2}")
    elif op == "+":
        print(f"The result is {n1+n2}")
    elif op == "-":
        print(f"The result is {n1-n2}")
    elif op == "*":
        print(f"The result is {n1*n2}")
    else:
        print("Enter a valid operation")
try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operation(+, -, *, /):").strip()
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Enter valid input(s)")

calculate(num1, operator, num2)