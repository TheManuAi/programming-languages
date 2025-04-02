try:
    number = int(input("Enter an integer: "))
    for n in range(1,11):
        print(f"{number} x {n} = {number*n}")
except ValueError:
    print("Enter a valid number")