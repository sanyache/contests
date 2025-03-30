class Solution:
    def maximumValue(self, s: List[str]) -> int:
        best = 0
        for num in s:
            if num.isdigit():
                best = max(best, int(num))
            else:
                best = max(best, len(num))
        return best