class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        set_avg = set()
        nums.sort()
        n = len(nums)
        for i in range(n//2):
            avg = (nums[n-1-i] + nums[i])/2
            set_avg.add(avg)
        return len(set_avg)