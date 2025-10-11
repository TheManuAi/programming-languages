n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = x[1:]
y = y[1:]

if len(set(x + y)) == n and set(x+y) == set(range(1, n+1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")