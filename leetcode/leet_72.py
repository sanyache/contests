def minDistance(word1, word2):
    n = len(word2)
    m = len(word1)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for j in range(1,m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1,m+1):
            if word1[j-1] == word2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) +1

    for row in dp:
        print(*row)
    return dp[-1][-1]


s1 = "horse"
s2 = "ros"
print(minDistance(s1, s2))

"""
'' -> ''           0
'' -> 'ab'         2
'ab' -> ''         2
'ab' -> 'ba'       2
'ab s' -> 'ba s'   2
'abc' -> 'bad'     3 
"""