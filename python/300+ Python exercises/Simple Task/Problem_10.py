try:
    num1 = int(input("Enter Maths marks: "))
    num2 = int(input("Enter Physics marks: "))
    num3 = int(input("Enter Chemistry marks: "))
    num4 = int(input("Enter English marks: "))
    num5 = int(input("Enter Computer Science marks: "))

    total = num1 + num2 + num3 + num4 + num5
    avg = total / 5

    print(f"\nYour Total marks are: {total}")
    print(f"And the Avg. marks are: {avg}")
except ValueError:
    print("Enter a valid number")