def change(amount, coins):
    cnt = [0] * (amount + 1)
    cnt[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            cnt[i] += cnt[i - coin]
        print(cnt)
    return cnt[-1]


amount = 5
coins = [1,2,5]
print(change(amount, coins))