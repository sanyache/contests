def costs(cost):
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = min(cost[1], cost[0] + cost[1])
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
    return min(dp[-1], dp[-2])

nums = [1,100,1,1,1,100,1,1,100,1]
print(costs(nums))