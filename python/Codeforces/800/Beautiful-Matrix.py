for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            r, c = i + 1, j + 1


moves = abs(r - 3) + abs(c - 3)
print(moves)
