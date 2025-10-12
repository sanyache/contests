n, k = map(int, input().split())
balls = [int(x) for x in input().split()]
balls.sort()
best = balls[k-1] - balls[0]
for i in range(1, n-k+1):
    best = min(best, balls[i+k-1] - balls[i])
print(best)