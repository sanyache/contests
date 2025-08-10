def coin_change(coins, amount):
    INF = float('inf')
    dp = [INF]*(amount+1)
    dp[0] = 0
    path = [1] * (amount+1)
    for val in range(1, amount+1):
        for coin in coins:
            if val - coin >=0:
                dp[val] = min(dp[val], dp[val-coin] +1)
                path[val] = coin
    # path as add option
    while amount >0:
        amount -= path[amount]
    return dp[-1] if dp[-1] != INF else -1

coins = [1,2,5]
amount = 11
print(coin_change(coins, amount))