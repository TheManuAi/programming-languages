import array as ar

try:
    num = ar.array("i", [])
    max = float("-inf")

    for i in range(5):
        num.append(int(input("Enter an number to store in the array: ")))

    for j in range (5):
        if num[j] > max:
            max = num[j]

    print(f"The Maximum in the array is {max}")
except ValueError:
    print("Enter a valid number!")