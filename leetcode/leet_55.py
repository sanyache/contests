def can_jump(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    for i in range(n-1):
        if dp[i]:
            for j in range(i, min(i+ nums[i]+1, n)):
                dp[j] = True
        if dp[n-1]:
            return True
    return dp[-1]

nums = [0,2,3]
print(can_jump(nums))