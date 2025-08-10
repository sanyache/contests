def rob(nums):
    n = len(nums)
    dp = [0]*(n+1)
    dp[1] = nums[0]
    for i in range(1,n):
        dp[i+1] = max(dp[i], dp[i-1] + nums[i])
    return dp[-1]

nums = [4, 11,10, 1, 2, 8, 5]
print(rob(nums))
