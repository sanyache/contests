n, k = map(int, input().split())
nums = [int(x) for x in input().split()]
cnt = [0]*11
for num in nums:
    cnt[num] += 1
min_val = 1001
for i in range(k+1):
    print(i)
    if cnt[i] < min_val:
        min_val = cnt[i]

print(min_val)