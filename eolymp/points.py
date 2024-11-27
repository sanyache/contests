from math import comb
n = int(input())
matrix = [[False for _ in range(1001)] for _ in range(1001)]
for _ in range(n):
    i, j = map(int, input().split())
    matrix[i][j] = True
total = 0
for i in range(1001):
    counter = 0
    for j in range(1001):
        if matrix[i][j]:
            counter +=1
    total += comb(counter, 3)
for j in range(1001):
    counter = 0
    for i in range(1001):
        if matrix[i][j]:
            counter +=1

    total += comb(counter, 3)

print(total)
