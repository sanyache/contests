class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix_sum = [0]*(n + 1)
        prefix_sum[n-1] = int(s[n-1])
        for i in range(n-1, -1, -1):
            prefix_sum[i] = int(s[i]) + prefix_sum[i+1]
        cnt_0 = 1 if s[0] == '0' else 0
        max_sc = cnt_0 + prefix_sum[1]
        for i in range(1, n-1):
            if s[i] == '0':
                cnt_0 += 1
            max_sc = max(max_sc, cnt_0 + prefix_sum[i+1])
        return max_sc