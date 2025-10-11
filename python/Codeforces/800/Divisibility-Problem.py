n = int(input())

result = []

for i in range(n):
    val1, val2 = map(int, input().split())
    if val1 % val2 == 0:
        result.append(0)
    else:
        move = val2 - (val1 % val2)
        result.append(move)

for i in result:
    print(i)