n = int(input())
lst = []
while n > 0:
    w = input()
    n -= 1
    lst.append(w)

for i in lst:
    if len(i) <= 10: 
        print(i)
    elif len(i) > 10:
        print(i[0]+str(len(i)-2)+i[-1])