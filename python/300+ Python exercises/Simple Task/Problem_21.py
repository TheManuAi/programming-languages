import array as ar

try:
    num = ar.array("i", [])
    min = float("inf")

    for i in range(5):
        num.append(int(input("Enter an number to store in the array: ")))

    for j in range (5):
        if num[j] < min:
            min = num[j]

    print(f"The Minimum in the array is {min}")
except ValueError:
    print("Enter a valid number!")