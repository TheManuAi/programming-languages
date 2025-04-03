lst = []

for i in range(1, 6):
    lst.append(input("Enter the {i} element: "))

print(f"This is the list: {lst}")
lst.clear()
print(f"Now the list is clear: {lst}")