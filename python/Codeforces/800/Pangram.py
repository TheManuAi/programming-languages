n = int(input())
l = input().lower()

if n < 26:
    print("NO")
else:
    sl = set(l)
    if len(sl) == 26:
        print("YES")
    else:
        print("NO")