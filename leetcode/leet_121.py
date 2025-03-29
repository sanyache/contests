class Solution:
    def maxProfit(self, a: List[int]) -> int:
        n = len(a)
        stack = list()
        stack.append(a[-1])
        best = 0
        for i in range(n-2, -1, -1):
            while stack and a[i] >= stack[-1]:
                stack.pop()
            stack.append(a[i])
            if len(stack) > 1:
                best = max((stack[0] - stack[-1]), best)
        return best