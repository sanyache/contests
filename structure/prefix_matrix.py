n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1 ,m+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + matrix[i-1][j-1] - prefix_sum[i-1][j-1]
k = int(input())
queries = [(int(q) for q in input().split()) for _ in range(k)]
for row in queries:
    r1, c1, r2, c2 = row
    print(prefix_sum[r2][c2] - prefix_sum[r2][c1-1] - prefix_sum[r1-1][c2] + prefix_sum[r1-1][c1-1])