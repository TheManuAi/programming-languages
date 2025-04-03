import array as ar

try:
    num = ar.array("i", [])
    total = 0

    for i in range(5):
        num.append(int(input("Enter an number to store in the array: ")))

    for j in range (5):
        total += num[j]

    print(f"The Sum of the array is {total}")
except ValueError:
    print("Enter a valid number!")