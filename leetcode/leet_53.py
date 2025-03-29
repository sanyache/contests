class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        best = nums[0]
        curr_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(curr_sum+nums[i], nums[i])
            best = max(best, curr_sum)
        return best