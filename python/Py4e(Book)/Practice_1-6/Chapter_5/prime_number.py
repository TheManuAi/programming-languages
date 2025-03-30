def prime():
    number = int(input("Generate prime numbers up to: "))
    if number < 2:
        print("No prime numbers available")
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

prime()