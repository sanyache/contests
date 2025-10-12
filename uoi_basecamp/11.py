from math import gcd

n = int(input())
cnt = 1
for i in range(1,n):
    cnt += n//i
print(cnt)
