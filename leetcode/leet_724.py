def pivotIndex(nums):
    s = sum(nums)
    left_s = 0
    for i in range(len(nums)):
        if left_s == s - left_s - nums[i]:
            return i
        left_s += nums[i]
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))