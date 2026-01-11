from math import gcd, lcm

n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
row1 = []
row2 = []
for row in matrix:
    row1.append(lcm(*row))
for j in range(m):
    curr = list()
    for i in range(n):
        curr.append(matrix[i][j])
    row2.append(lcm(*curr))

LIM = pow(10, 9)
for i in range(n):
    curr = list()
    for j in range(m):
        if row1[i] > LIM or row2[j] > LIM:
            print(-1)
            exit()
        curr.append(gcd(row1[i], row2[j]))
    if curr != matrix[i]:
        print(-1)
        exit()
print(*row1)
print(*row2)