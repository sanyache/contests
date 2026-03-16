def longestCommonSubsequence(text1, text2):
    n = len(text2)
    m = len(text1)

    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if text2[i-1] == text1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for row in dp:
        print(*row)
    return dp[-1][-1]


text1 = "vista"
text2 = "hish"

print(longestCommonSubsequence(text1, text2))
