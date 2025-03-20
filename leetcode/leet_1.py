class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = dict()
        for val in nums:
            if n_map.get(val):
                n_map[val] += 1
            else:
                n_map[val] = 1

        for i in range(len(nums)):
            n_map[nums[i]] -= 1
            if target - nums[i] in n_map and n_map[target - nums[i]]>0:
                return[i, nums.index(target-nums[i], i+1)]