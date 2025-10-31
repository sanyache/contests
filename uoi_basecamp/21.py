nums = [int(x) for x in input()]
s = 0
if nums[0] == nums[2]:
    for i in range(10):
        s += nums[0]*100 + i*10 + nums[2]
    s -= nums[0]*100 + nums[1]*10 + nums[2]
elif nums[2] == 0:
    s = nums[0]*100 + nums[1]*10 + nums[1]
else:
    s = nums[2]*100 + nums[1]*10 + nums[2] + nums[0] * 100 + nums[1] * 10 + nums[0]

print(s)