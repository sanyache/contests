nums = [int(x) for x in input().split()]
nums.sort()
l = nums[0]
r = nums[-1]
if l < 0 < r:
    print((abs(l) + r) * 2)
elif l < 0:
    print(abs(l)*2)
elif r >= 0:
    print(r*2)

