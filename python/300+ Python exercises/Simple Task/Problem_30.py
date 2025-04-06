try:
    num = float(input("Enter a number: "))
    if num % 2 == 0 and num % 3 == 0:
        print(f"The {num} is divisible by 2 and 3")
    elif num % 5 == 0 and num % 6 == 0:
        print(f"The {num} is divisible by 5 and 6") 
    else:
        print(f"{num} is not divisible by (2 and 3) nor by (5 and 6)")
except ValueError:
    print("Enter a valid number!")