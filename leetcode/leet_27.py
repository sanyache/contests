def rem_elements(nums, k):
    right = len(nums)-1
    left = 0
    while left < right:
        if nums[left] != k:
            left += 1
            continue
        while right > left:
            if nums[right] != k:
                break
            right -= 1

        nums[left], nums[right] = nums[right], nums[left]
        left +=1
    i = 0
    while i < len(nums):
        if nums[i] != k:
            i += 1
        else:
            break
    return i


nums = [0,1,2,2,3,0,4,2]
val = 2
print(rem_elements(nums, val))