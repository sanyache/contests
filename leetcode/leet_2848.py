def points(nums):
    nums.sort(key = lambda x: x[0])
    n = nums[0][1] - nums[0][0] + 1
    prev_ind = 0
    for i in range(1, len(nums)):
        if nums[i][1] > nums[prev_ind][1]:
            if nums[i][0] <= nums[prev_ind][1]:
                n += nums[i][1] - nums[prev_ind][1]
            else:
                n += nums[i][1] - nums[i][0] + 1
            prev_ind = i
    return n

nums = [[2,3],[3,9],[5,7],[4,10],[9,10]]