"""
Полярники переправляються через річку на двомісному човні
Час зараховується по самому повільному.
Дано кількість полярників і час за який вони
можуть переправится
Вивести мінімальний час
4 1 6 7 8
23
"""
n, data = input().split(' ', 1)
n = int(n)
speeds = [int(x) for x in data.split()]
speeds.sort()
dp = [0]*n
dp[0] = speeds[0]
dp[1] = speeds[1]
for i in range(2, n):
    dp[i] = min(dp[i-1]+speeds[i] + speeds[0],
                dp[i-2] + speeds[i]+speeds[0]+speeds[1]*2)
print(dp[n-1])