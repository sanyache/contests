import heapq

def maxSub(nums, k):
    hp = []
    rez = []
    for i in range(len(nums)):
        hp.append((-nums[i], i))
    heapq.heapify(hp)
    curr = heapq.nsmallest(k, hp)

    for val, ind in sorted(curr, key=lambda x: x[1]):
        rez.append(nums[ind])
    return rez


nums = [-1, -2, 3, 4]
k = 3
print(maxSub(nums, k))
