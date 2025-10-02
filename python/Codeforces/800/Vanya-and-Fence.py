n, h = map(int, input().split())

frnds = list(map(int, input().split()))

count = 0

for i in frnds:
    if i <= h:
        count += 1
    else:
        count += 2

print(count)