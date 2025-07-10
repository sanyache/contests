def serch(nums):
    l = 0
    r = len(nums)-1
    while r>=l:
        mid = (r+l)//2
        if 0 < mid<len(nums)-1 and  nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        if nums[mid] < nums[mid+1]:
            l = mid+1
        else:
            r = mid-1
    return l

nums = [20, 23, 34, 56, 78, 90, 98, 73, 67, 12, 7]
print(serch(nums))