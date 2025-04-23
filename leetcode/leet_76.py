class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l_min = 0
        r_min = len(s)
        l = 0
        map_t = Counter(t)
        curr_map = dict()
        curr_sum = 0
        for r in range(len(s)):
            if s[r] in map_t:
                if curr_map.get(s[r]):
                    curr_map[s[r]] += 1

                else:
                    curr_map[s[r]] = 1
                if curr_map[s[r]] <= map_t[s[r]]:
                    curr_sum += 1

            while curr_sum == len(t):
                if curr_map.get(s[l]):
                    if curr_map[s[l]] == map_t[s[l]]:
                        if r-l < r_min - l_min:
                            r_min = r
                            l_min = l
                        curr_sum -= 1
                    curr_map[s[l]] -= 1
                l += 1

        if r_min - l_min == len(s):
            return ""
        return s[l_min:r_min+1]