n,m,k = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    matrix[n-x][y-1] = -1
for i in range(n-2, -1, -1):
    if matrix[i][0] == -1:
        break
    matrix[i][0] = 1
    for j in range(1, n):
        if matrix[i][j] == -1:
            break
        matrix[i][j] = 1
for j in range(1, m):
    if matrix[n-1][j] == -1:
        break
    matrix[n-1][j] = 1
    for i in range(n-1, -1, -1):
        if matrix[i][j] == -1:
            break
        matrix[i][j] = 1
counter = 0
for row in matrix:
    counter += row.count(1)
print(counter)

