def prime():
    number = int(input("How many prime numbers do you want: "))
    prime_list = []
    prime_num = 2
    while len(prime_list) < number:
        if prime_num > 1 and all(prime_num % i != 0 for i in range(2, int(prime_num**0.5)+1)):
            prime_list.append(prime_num)
        prime_num += 1
    print(f"The required prime numbers: {prime_list}")
prime()