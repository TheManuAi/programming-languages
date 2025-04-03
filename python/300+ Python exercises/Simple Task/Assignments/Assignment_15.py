tup = ()
for i in range(1, 6):
    tup += (float(input(f"Enter the {i} element: ")),)

print(f"The tuple is {tup}")
tup = ()
print(f"Now the tuple is clear: {tup}")