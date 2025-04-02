number = input("Enter an integer to square: ")
try:
    square = int(number)
    print("Number\tSquare")
    for i in range(1, square + 1):
        print(f"{i}\t{i**2}")
except ValueError:
    print("Enter a valid number")