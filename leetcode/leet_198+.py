def rob(nums):
    n = len(nums)
    dp = [0]*(n+1)
    dp[1] = nums[0]
    for i in range(1,n):
        dp[i + 1] = nums[i] + max(dp[i - 1], dp[i - 2])
    return max(dp[-1], dp[-2])

nums = [4, 11,10, 1, 2, 8, 5]
print(rob(nums))