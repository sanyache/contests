def word_break(s, wordDict):
    n = len(s)
    words = set(wordDict)
    dp = [False] * (n+1)
    dp[0] = True
    for i in range(n):
        j = i
        while j >= 0:
            if dp[j] and s[j:i+1] in words:
                dp[i+1] = True
            j -=1
    return dp[-1]


s = "goalspecial"
wordDict = ["go","goal","goals","special"]
print(word_break(s,wordDict))