try:
    num = float(input("Enter a number to cube: "))
    print(f"The cube of {num} is {num ** 3}")
except ValueError:
    print("Enter a valid number!")