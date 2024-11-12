"""
6
3 4 12 6 14 13
5
"""
n = int(input())
nails = [int(x) for x in input().split()]
nails.sort()
dist = [0]*n
dist[0] = 10001
dist[1] = nails[1] - nails[0]
for i in range(2, n):
    dist[i] = min(dist[i-2], dist[i-1]) + nails[i] - nails[i-1]
print(dist[n-1])
