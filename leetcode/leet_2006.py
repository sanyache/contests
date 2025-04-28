class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        map_nums = dict()
        cnt = 0
        for num in nums:
            curr = map_nums.get(abs(k-num))
            curr2 = map_nums.get((k+num))
            if curr and num - abs(k-num) == k:
                cnt += curr
            if curr2:
                cnt += curr2
            if map_nums.get(num):
                map_nums[num] += 1
            else:
                map_nums[num] = 1
        return cnt