try:
    number = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    for n in range(1,11):
        print(f"{number} x {n} = {number*n} \t {number2} x {n} = {number2*n}")
except ValueError:
    print("Enter a valid number")