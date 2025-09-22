n = int(input())
result = 0

while n > 0:
    w = input()
    if w[0:2] == "++" or w[1:3] == "++":
        result += 1
    elif w[0:2] == "--" or w[1:3] == "--":
        result -= 1
    n -= 1

print(result)