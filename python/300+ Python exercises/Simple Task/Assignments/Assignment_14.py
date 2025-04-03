try:
    tup = ()
    n = int(input("How many numbers have you got: "))
    for i in range(1, n+1):
        tup += (float(input(f"Enter the {i} number: ")),)

    print(f"The sum of these {n} number is {sum(tup)}")
except ValueError:
    print("Enter a valid number")