nums = [int(x) for x in input().split()]

cnt = 1
for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] == nums[i]:
            break
    else:
        cnt += 1

sort_arr = sorted(nums)
cnt2 = 1
for i in range(1, len(sort_arr)):
    if sort_arr[i-1] != sort_arr[i]:
        cnt2 += 1

map_nums = dict()

for num in nums:
    if num in map_nums:
        map_nums[num] += 1
    else:
        map_nums[num] = 1

print(cnt)
print(cnt2)
print(len(map_nums))
print(len(set(nums)))
