try:
    print("For this equation -> (a+b+c)(a/b)(2a+3b), enter numbers")

    num1 = float(input("Enter the first number(a): "))
    num2 = float(input("Enter the second number(b): "))
    num3 = float(input("Enter the third number(c): "))

    solution = (num1 + num2 + num3) * (num1 / num2) * (2 * num1 + 3 * num2)
    print(f"The solution is {round(solution, 2)}")

except ValueError:
    print("Enter a valid number")