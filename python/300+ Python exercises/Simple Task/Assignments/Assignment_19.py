try:
    print("For this equation -> (d+a)+(2ab/d)(4c+10), enter numbers")

    num1 = float(input("Enter the first number(a): "))
    num2 = float(input("Enter the second number(b): "))
    num3 = float(input("Enter the third number(c): "))
    num4 = float(input("Enter the forth number(d): "))

    solution = (num4 + num1) + (2 * num1 * num2 / num4) * (4 * num3 + 10)
    print(f"The solution is {round(solution, 2)}")

except ValueError:
    print("Enter a valid number")