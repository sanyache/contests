n, m = map(int, input().split())
to_buy = [int(x) for x in input().split()]
to_sell = [int(x) for x in input().split()]
to_buy.sort()
to_sell.sort(reverse=True)
s = 0
for i in range(min(len(to_buy), len(to_sell))):
    if to_sell[i] - to_buy[i] > 0:
        s += to_sell[i] - to_buy[i]

print(s)