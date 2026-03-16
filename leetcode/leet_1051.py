def sort(nums):
    cnt = 0
    m = max(nums)
    freq = [0]*(m+1)
    for num in nums:
        freq[num] += 1
    k = 0
    for i in range(1, m+1):
        for j in range(freq[i]):
            if nums[k] != i:
                cnt += 1
            k += 1
    return cnt

heights = [1,1,4,2,1,3]
print(sort(heights))
