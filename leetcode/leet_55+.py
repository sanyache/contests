def can_jump(nums):
    n = len(nums)
    if n == 1:
        return True
    max_jump  = 1
    for i in range(n):
        max_jump = max(max_jump-1, nums[i])
        if max_jump == 0:
            return False
        if max_jump + i >= n-1:
            return True
    return True

nums = [0]
print(can_jump(nums))