"""
Знайти максимальну кількість членів команди,
показник скілів яких не перевищує k
Input:
5
1 10 17 12 15 2
"""
k = int(input())
team = [int(x) for x in input().split()]
team.sort()
max_k = 0
l =0
for r in range(1, len(team)):
    while team[r] - team[l] > k:
        l += 1
    max_k = max(max_k, r-l+1)
print(max_k)