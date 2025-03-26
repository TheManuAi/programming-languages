num1 = int(input("Enter the first number: "))
operator = input("Enter the operator(+, -, /, *): ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    result = num1 / num2
elif operator == "*":
    result = num1 * num2
else:
    print("Error: Invalid operator.")

print(f"The result of {num1} {operator} {num2} = {result}")