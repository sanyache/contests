import heapq

def maxSub(nums, k):
    rez = list()
    curr = list()
    for ind, val in enumerate(nums):
        curr.append((val, ind))
    curr.sort(key=lambda x: x[0])
    for val, ind in sorted(curr[-k:], key=lambda x: x[1]):
        rez.append(nums[ind])
    return rez



nums = [-1, -2, 3, 4]
k = 3
print(maxSub(nums, k))
