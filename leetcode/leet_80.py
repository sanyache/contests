class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        l = 0
        cnt = 0
        curr =nums[0]
        for r in range(1, len(nums)):
            if curr < nums[r]:
                nums[l + 1] = nums[r]
                l += 1
                cnt = 0
                curr = nums[r]
            elif curr == nums[r] and cnt<1:
                nums[l + 1] = nums[r]
                l += 1
                cnt += 1
        return l + 1