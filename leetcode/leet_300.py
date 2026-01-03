def len_sub(nums):
    n = len(nums)
    dp = [1] * n
    best = 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
              dp[i] = max(dp[i], dp[j]+1)
              best = max(best, dp[j]+1)
    return best


nums = [10,9,2,5,3,7,101,18]
print(len_sub(nums))