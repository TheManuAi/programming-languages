n = int(input())
count = 0

while n > 0:
    r = input()
    if (int(r[0]) == 1 and int(r[2]) == 1) or (int(r[2]) == 1 and int(r[-1]) == 1) or (int(r[0]) == 1 and int(r[-1]) == 1):
        count += 1
    n -= 1

print(count)