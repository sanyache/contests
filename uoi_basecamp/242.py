n, m = map(int, input().split())
canvas = [['.' for _ in range(m)] for _ in range(n)]
l = 0
r = m-1
tact = 0
for i in range(n):
    for j in range(m):
        if j == l or j == r:
            canvas[i][j] = 'x'
    if l == m-1 or l == 0 and i != 0:
        tact += 1
    if tact%2 == 0:
        l += 1
        r -= 1
    else:
        l -= 1
        r += 1
for row in canvas:
    print(''.join(row))