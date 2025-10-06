n1 = input()
n2 = input()

a = ""
for i in range(len(n1)):
    if n1[i] == n2[i]:
        a += "0"
    else: 
        a += "1"
print(a)