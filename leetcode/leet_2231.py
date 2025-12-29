import heapq


def largestInteger(n: int) -> int:
    nums = [int(x) for x in str(n)]
    l = len(nums)
    for k in range((l // 2) + 1 ):
        max_ind = k
        max_el = nums[k]
        remainder = nums[k] % 2
        for i in range(k+1, l):
            if nums[i] % 2 == remainder and nums[i] >= max_el:
                max_el = nums[i]
                max_ind = i
        if max_el != nums[k]:
            nums[k], nums[max_ind] = nums[max_ind], nums[k]
        print(nums)
    s = ''
    for num in nums:
        s += str(num)
    return int(s)

n = 568

print(largestInteger(n))





