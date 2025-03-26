num = float(input("Enter a number to check weather positive, negative or zero: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
elif num < 0:
    print("Negative number")
else:
    print("Invalid input")