def factorail(n):
    if n > 0:
        for i in range(1, n):
            n *= i
        print(f"The factorial is {n}")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        print("Please enter a positive number")

factorail(n= int(input("Enter a number: ")))