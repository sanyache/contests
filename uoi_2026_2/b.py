
n = int(input())
nums = [int(x) for x in input().split()]
s = sum(nums)

for k in range(n, 1, -1):
    if s%k != 0:
        continue
    d = s//k
    curr_s = 0
    for i in range(n):
        curr_s += nums[i]
        if curr_s == d and i != n-1:
            curr_s = 0
        if curr_s > d:
            break
    else:
        if curr_s == d:
            print(k - 1)
            exit()
print(0)

