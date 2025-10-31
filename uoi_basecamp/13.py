n, m = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    s = (i * (1 + i))//2
    if s%m == 0:
        cnt += 1
        print(i, s)
print(cnt)