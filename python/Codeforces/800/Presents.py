n = int(input())

p = list(map(int, input().split()))
g = [0] * n

for i in range(n):
    gr = i + 1
    r = p[i]
    g[r-1] = gr

print(*g)

# 2 3 4 1
# 1 2 3 4

# 1 - 2
# 2 - 3
# 3 - 4
# 4 - 1

# 4 1 2 3