def nextGreaterElement(nums):
    n = len(nums)
    stack = list()
    best = 0
    for i in range(n):
        if not stack or nums[i] < nums[stack[-1]]:
            stack.append(i)
    for i in range(n-1, -1, -1):
        while stack and  nums[i] >= nums[stack[-1]]:
            curr = stack.pop()
            best = max(best, i-curr)
    return best
nums = [9,8,8,8,4,3,3,7,1,1,1,5,1,1]
print(nextGreaterElement(nums))