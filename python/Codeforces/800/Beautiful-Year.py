y = int(input())
y += 1

while True:
    if len(str(y)) == len(set(str(y))):
        print(y)
        break
    else: y += 1