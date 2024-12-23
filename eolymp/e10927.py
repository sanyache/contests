n, m = map(int, input().split())
changes = []
arr = []
for i in range(m):
    x, y = map(int, input().split())
    changes.append((x, y))
changes.sort(key=lambda e: -e[1])
top = 0
for count, val in changes:
    arr.extend([val]*min(count, n - top))
    top += count
    print(sum(arr))