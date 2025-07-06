def nextGreaterElement(nums):
    n = len(nums)
    max_suf = [0]*n
    max_suf[-1] = nums[-1]
    for i in range(n-2, -1, -1):
        max_suf[i] = max(nums[i], max_suf[i+1])
    l = 0
    best = 0
    for r in range(n):
        while nums[l] > max_suf[r]:
            l += 1
        best = max(best, r-l)
    return best
nums = [9,8,8,8,4,3,3,7,1,1,1,5,1,1]
print(nextGreaterElement(nums))