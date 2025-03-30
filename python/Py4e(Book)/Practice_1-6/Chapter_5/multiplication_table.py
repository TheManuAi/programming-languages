try:
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Enter a valid number")