n = int(input())

count = 1
p = input()

for i in range(n-1):
    c = input()
    if c != p:
        count += 1
    p = c

print(count)