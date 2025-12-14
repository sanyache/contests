def jump(nums) -> int:
    n = len(nums)
    if n <= 1:
        return 0
    cnt = 0
    current_end = 0
    max_jump = 0

    for i in range(n - 1):
        max_jump = max(max_jump, i + nums[i])
        if i == current_end:
            cnt += 1
            current_end = max_jump

    return cnt

nums = [3,4,3,2,5,4,3]
print(jump(nums))