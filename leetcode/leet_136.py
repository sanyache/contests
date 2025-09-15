def single_number(nums):
    nums.sort()
    i = 0
    while i < len(nums) -1:
        if nums[i] != nums[i+1]:
            return nums[i]
        i += 2
    return nums[-1]

nums = [4,1,2,1,2]
print(single_number(nums))