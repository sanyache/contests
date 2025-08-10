def decoding(s):
    if len(s) == 0 or s[0] == '0':
        return 0
    dp = [1,1]
    for i in range(1, len(s)):
        curr = 0
        if s[i] != '0':
            curr += dp[-1]
        if s[i-1] != '0'  and int(s[i-1] + s[i]) < 27:
            curr += dp[-2]
        if curr == 0:
            return 0
        dp.append(curr)
    return dp[-1]

s = "2101"
print(decoding(s))