class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        cnt = 0
        s_map = set()
        for r in range(len(s)):
            while s[r] in s_map:
                s_map.remove(s[l])
                l +=1
            s_map.add(s[r])

            if r-l+1 == 3:
                cnt += 1
                s_map.remove(s[l])
                l += 1
        return cnt