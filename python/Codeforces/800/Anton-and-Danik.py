n = input()
g = input()

a = 0
d = 0
for i in g:
    if i == "A":
        a += 1
    else: 
        d += 1


if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")