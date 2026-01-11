def curr_sum(nums, m):
    s = 0
    for num in nums:
        if num - m > 0:
            s += num - m
    return s


n, k = map(int, input().split())
nums = [int(x) for x in input().split()]
l = 0
r = max(nums)

while r >= l:
    mid = (r+l)//2
    s = curr_sum(nums, mid)

    if s == k:
        print(mid)
        exit()
    if s > k:
        l = mid +1
    else:
        r = mid -1
print(r)
