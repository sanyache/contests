def leftRightDifference(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left_s = 0
    right_s = sum(nums)
    answer = [0] * n
    for i in range(n):
        answer[i] = abs(left_s - right_s + nums[i])
        left_s += nums[i]
        right_s -= nums[i]
    return answer