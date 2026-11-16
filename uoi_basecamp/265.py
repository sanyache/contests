from collections import deque

def bfs(row, col):
    dist = [[-1] * m for _ in range(n)]
    dist[row][col] = 0
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((row, col))
    while q:
        data = q.popleft()
        x = data[0]
        y = data[1]

        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < n and 0 <= dy < m and field[dx][dy] != 'F'  and dist[dx][dy] == -1:
                q.append((dx, dy))
                dist[dx][dy] = dist[x][y] + 1

                bad_dist[dx][dy] = max(bad_dist[dx][dy], dist[dx][dy])


n, m = map(int, input().split())
field = [['.']*m for _ in range(n)]
holes = []
bad_dist = [[0]*m for _ in range(n)]
for i in range(n):
    r = input()
    for j in range(m):
        if r[j] == 'F':
            field[i][j] = 'F'
        elif r[j] == 'H':
            field[i][j] = 'H'
            holes.append((i, j))

best = n*m
rez = list()
for i, j in holes:
    bfs(i, j)

for i in range(n):
    for j in range(m):
        if field[i][j] != 'F':
            if bad_dist[i][j] < best:
                rez = list()
                rez.append((i+1,j+1))
                best = bad_dist[i][j]
            elif bad_dist[i][j] == best:
                rez.append((i+1, j+1))

print(len(rez))
for val in rez:
    print(* val)
