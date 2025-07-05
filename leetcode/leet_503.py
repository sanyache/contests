def nextGreaterElement(nums):
    nums = nums + nums
    n = len(nums)
    greater = [-1] *n
    stack = list()
    for i in range(n-1, -1, -1):
        while stack and nums[i] >= stack[-1]:
            stack.pop()
        if stack:
            greater[i] = stack[-1]
        else:
            greater[i] = -1
        stack.append(nums[i])
    stack.clear()

    return greater[:n//2]

nums = [5,4,3,2,1]
print(nextGreaterElement(nums))
