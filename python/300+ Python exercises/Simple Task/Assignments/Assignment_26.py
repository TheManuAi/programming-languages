try:
    num = int(input("Enter a integer: "))
    if num % 2 == 0:
        print(f"The {num} is Even")
        print(f"And the square of {num} is {num ** 2}")
    else:
        print(f"The {num} is Odd")
        print(f"The square of {num} is {num ** 2}")
except ValueError:
    print("Enter a valid integer")