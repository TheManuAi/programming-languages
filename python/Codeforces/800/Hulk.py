n = int(input())

p = ""

for i in range(1, n+1):
    if i % 2 != 0:
        p += "I hate"
    else:
        p += "I love"

    if i != n:
        p += " that "

p += " it"

print(p)