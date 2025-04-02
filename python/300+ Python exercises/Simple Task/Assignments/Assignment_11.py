try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    print(f"The greatest number is {max(num1, num2, num3)}")
    if num1 == num2 == num3:
        print("They all are equal")
except ValueError:
    print("Enter a valid number!")