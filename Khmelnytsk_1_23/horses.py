"""
Input:
2 3
1 2 3 4 5 6 7 8 9 10 11 12
Output:
1
Input:
2 2
3 1 3 3 3 3 3 3
Output:
2
"""
n, k = map(int, input().split())
speeds = [int(x) for x in input().split()]
speeds.sort()
print(speeds[:2*n])
