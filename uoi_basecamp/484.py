from collections import deque

def calculate_dp(dp, x, y):
    if x == 0 or y == 0:
        return  1
    else:
        calc_val = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1
    return calc_val

n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]

max_side = 0
answers = [0]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    q = deque()
    matrix[x][y] = 1
    dp[x][y] = calculate_dp(dp, x, y)
    max_side = max(max_side, dp[x][y])
    q.append((x,y))
    moves = [(1,0), (0, 1), (1,1)]
    while q:
        i, j = q.popleft()
        for dx, dy in moves:
            x = i + dx
            y = j + dy
            if 0 <= x < n and 0 <= y < n and matrix[x][y] == 1:
                old_dp = dp[x][y]
                new_dp = calculate_dp(dp, x, y)
                if old_dp != new_dp:
                    q.append((x,y))
                    dp[x][y] = new_dp
                    max_side = max(max_side, new_dp)

    answers.append(max_side)

for a in answers:
    print(a)
