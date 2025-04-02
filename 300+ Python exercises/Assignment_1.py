number = input("Enter an integer to square and cube: ")
try:
    square = int(number)
    print("Number\tSquare\tCube")
    for i in range(1, square + 1):
        print(f"{i}\t{i**2}\t{i**3}")
except ValueError:
    print("Enter a valid number")