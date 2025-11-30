n = int(input())
c = [int(i) for i in input().split()]
best = 0
cnt = 0
for i in range(n):
    if c[i] == 2:
        cnt += 1

    else:
        cnt = 0
    best = max(best, cnt * 2)
print(max(best, n))