def maximalSquare( matrix):
    max_l = 0
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0 for _ in range(m+1)] for _ in range(n+1) ]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            max_l = max(max_l, dp[i][j])
    for row in dp:
        print(*row)
    return max_l**2

matrix = [["1","0","1","1","0","1"],
          ["1","1","1","1","1","1"],
          ["0","1","1","0","1","1"],
          ["1","1","1","0","1","0"],
          ["0","1","1","1","1","1"],
          ["1","1","0","1","1","1"]]


print(maximalSquare(matrix))
