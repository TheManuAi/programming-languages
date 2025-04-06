try:
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"The {num} is Positive")
    elif num < 0:
        print(f"The {num} is Nagative")
    else:
        print("The number is 0")      
except ValueError:
    print("Enter a valid number!")