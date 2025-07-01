def minSubArrayLen(target, nums):
    best = len(nums)+1
    s = 0
    l = 0
    for r in range(len(nums)):
        s += nums[r]
        while s >= target:
            best = min(best, r - l + 1)
            s -= nums[l]
            l += 1
    return best if best <= len(nums) else 0

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))