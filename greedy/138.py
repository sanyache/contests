n = int(input())
coins = [500, 200, 100, 50, 20, 10]
cnt = 0
for coin in  coins:
    cnt += n//coin
    n %= coin
if n != 0:
    print(-1)
else:
    print(cnt)
