class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        cnt_1 = 0
        for i in range(1, n):
            if s[i] == '1':
                cnt_1 += 1
        cnt_0 = 1 if s[0] == '0' else 0
        best = cnt_0 + cnt_1
        for i in range(1, n - 1):
            if s[i] == '0':
                cnt_0 += 1
            else:
                cnt_1 -= 1
            best = max(best, cnt_0 + cnt_1)

        return best