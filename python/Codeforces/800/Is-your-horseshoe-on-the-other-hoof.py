c = list(input().split())

cu = set(c)

if len(c) == len(cu):
    print(0)
elif (len(c) - len(cu)) == 1:
    print(1)
elif (len(c) - len(cu)) == 2:
    print(2)
else:
    print(3)