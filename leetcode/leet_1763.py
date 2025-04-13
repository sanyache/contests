class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best = ''
        for l in range(len(s)):
            map_lower = set()
            map_upper = set()
            for r in range(l, len(s)):
                if s[r].islower():
                    map_lower.add(s[r])
                else:
                    map_upper.add(s[r].casefold())
                if map_upper == map_lower and r-l+1>len(best):
                    best = s[l:r+1]
        return best