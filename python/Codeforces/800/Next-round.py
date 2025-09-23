n, k = map(int, input().split()) 
s = list(map(int, input().split()))

count = 0

for i in s:
    if i >= s[k-1] and i > 0:
        count += 1

print(count)