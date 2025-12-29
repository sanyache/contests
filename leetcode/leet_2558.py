import heapq
import math

def pickGifts(gifts, k):
    nums = [-x for x in gifts]
    heapq.heapify(nums)
    for _ in range(k):
        curr = heapq.heappop(nums) * (-1)
        heapq.heappush(nums, - int(math.sqrt(curr)))
    s = 0
    for num in nums:
        s += -num

    return s


gifts = [25,64,9,4,100]
k = 4

print(pickGifts(gifts ,k))





