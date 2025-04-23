class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_s = set()
        best = 0
        l = 0
        for r in range(len(s)):
            while s[r] in map_s:
                map_s.remove(s[l])
                l +=1
            map_s.add(s[r])
            best = max(best, r-l+1)
        return best