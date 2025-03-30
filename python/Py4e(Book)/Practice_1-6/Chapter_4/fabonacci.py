def fabonacci():
    num = int(input("Enter a number: "))
    a, b = 0, 1
    count = 0
    if num <= 0:    
        print("Please enter a positive integer")
    elif num == 1:
        print(f"Fibonacci sequence upto {num}: {a}")
    else:   
        print("Fibonacci sequence:")
        while count < num:
            print(a, end=' ')
            nth = a + b
            a = b
            b = nth
            count += 1
    
fabonacci()