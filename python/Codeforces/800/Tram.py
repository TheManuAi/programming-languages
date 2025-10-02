n = int(input())

maxm = 0
cur = 0
for i in range(n):
    val1, val2 = map(int, input().split())
    cur -= val1
    cur += val2
    if cur > maxm:
        maxm = cur

print(maxm)