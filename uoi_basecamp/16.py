n = int(input())
rect = list()
for _ in range(n):
    a,b = map(int, input().split())
    if a > b:
        a,b = b,a
    rect.append((a,b))
rect.sort(key=lambda x: (x[0], x[1]))
print(rect)
max_suff = rect[-1][1]
suff = [max_suff] * n
for i in range(n-2, -1, -1):
    suff[i] = max(rect[i][1], suff[i+1])
print(suff)
cnt = 0
for i in range(n-1):
    if suff[i+1] >= rect[i][1]:
        cnt += 1
print(cnt)