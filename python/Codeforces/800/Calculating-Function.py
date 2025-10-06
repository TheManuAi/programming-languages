# The give code below is correct but it will take too much time for a number 10^15 
'''n = int(input())
total = 0

for i in range(1, n+1):
    if i % 2 == 0:
        total += i
    else:
        total -= i

print(total) '''

# here's the code which will run fast 
n = int(input())

if n % 2 == 0:
    print(n//2)
else:
    print(-(n+1)//2)