n = int(input())

count = 0

for i in range(n):
    val1, val2 = map(int, input().split())
    if (val2-val1) >= 2:
        count += 1

print(count)