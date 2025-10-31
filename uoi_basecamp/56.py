nums = [int(x) for x in input()]
t = nums[0]
if len(set(nums)) != 1:
    cnt = 0
    for i in range(len(nums)- 1):
        if nums[i+1] - nums[i] == 1:
            cnt += 1
    if cnt == 3:
        print('Yes')
    else:
        print('No')
else:
    print('Yes')