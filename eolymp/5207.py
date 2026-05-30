from array import array

s = input()
n = len(s)
dp = [array('I', [0] * n) for _ in range(n)]
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if i == j:
            dp[i][j] = 1
            continue
        if s[i] == s[j]:
            dp[i][j] = 2 + dp[i + 1][j - 1]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

l = 0
r = n-1
p = ""
while l < r:
    if s[l] == s[r]:
        p += s[l]
        l += 1
        r -= 1
    elif dp[l][r-1] > dp[l+1][r]:
        r -= 1
    else:
        l += 1
if l == r:
    p += s[l] + p[::-1]
else:
    p += p[::-1]
print(p)
