try:
    num = int(input("Enter a integer: "))
    if num % 2 == 0:
        print(f"The {num} is Even")
    else:
        print(f"The {num} is Odd")
except ValueError:
    print("Enter a valid integer")