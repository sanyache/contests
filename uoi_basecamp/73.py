nums = [1 if x == "B" else 0 for x in input()]
cnt = 0
n = len(nums)
i = 0
while i < n-1:
    if nums[i] + nums[i+1] == 1:
        cnt += 1
        i += 2
    else:
        i +=1
print(cnt)
