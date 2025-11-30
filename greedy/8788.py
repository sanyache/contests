n, s = map(int, input().split())
cnt = 0
for val in range(n, 0, -1):
    cnt += s//val
    s %= val
    if s == 0:
        break
print(cnt)
