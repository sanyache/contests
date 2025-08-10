def min_path(grid):
    n = len(grid)
    m = len(grid[0])
    val = [[0]*m for _ in range(n)]
    val[0][0] = grid[0][0]
    for i in range(1,n):
        val[i][0] = val[i-1][0] + grid[i][0]
    for j in range(1,m):
        val[0][j] = val[0][j-1] + grid[0][j]
    for i in range(1,n):
        for j in range(1,m):
            val[i][j] = min(val[i-1][j], val[i][j-1]) + grid[i][j]
    return val[n-1][m-1]

grid =  [[1,3,1],[1,5,1],[4,2,1]]
print(min_path(grid))