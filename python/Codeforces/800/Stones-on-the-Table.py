n = int(input())
w = list(input())

count = 0

for i in range(n):
    if i < n-1:
        if w[i] == w[i+1]:
            count += 1

print(count)