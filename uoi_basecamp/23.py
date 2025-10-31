n = int(input())
nums = [int(x) for x in input().split()]
nums[-1] = abs(nums[-1])
for i in range(n-2, -1, -1):
    if abs(nums[i]) < nums[i+1]:
        nums[i] = abs(nums[i])
        continue
    if nums[i] > nums[i+1]:
        nums[i] *= -1
    if nums[i] > nums[i + 1]:
        print("NO")
        break
else:
    print("YES")
    print(*nums)


