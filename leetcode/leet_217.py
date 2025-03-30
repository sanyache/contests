class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map_nums = set(nums)
        return len(nums) != len(map_nums)