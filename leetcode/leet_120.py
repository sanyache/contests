def min_path(triangle):
    n = len(triangle)
    dp = [[0]*len(triangle[i]) for i in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        m = len(triangle[i])
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
        for j in range(1, m-1):
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return min(dp[-1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(min_path(triangle))