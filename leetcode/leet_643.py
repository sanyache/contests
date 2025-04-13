class Solution:
    def findMaxAverage(self, a: List[int], k: int) -> float:
        curr_sum = sum(a[:k])
        max_avg = curr_sum/k
        for i in range(k, len(a)):
            curr_sum = curr_sum - a[i-k] + a[i]
            max_avg = max(max_avg, curr_sum/k)

        return float(f"{max_avg:.5f}")