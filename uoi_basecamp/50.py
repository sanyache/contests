l, r = map(int, input().split())
cnt = 0
for num in range(l, r+1):
    if '5' not in str(num):
        cnt += 1
print(cnt)