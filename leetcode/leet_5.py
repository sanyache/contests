def maxPalindrom(s):
    def get_palindrom(l, r):
        # if s[l] != s[r]:
        #     return s[r]
        while l>=0 and r<n and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]
    rez = ''
    n = len(s)
    for i in range(0, n):
        palindrom = get_palindrom(i, i+1)
        if len(rez) < len(palindrom):
            rez = palindrom
        palindrom = get_palindrom(i, i)
        if len(rez) < len(palindrom):
            rez = palindrom
    return rez
s = "abba"
print(maxPalindrom(s))

