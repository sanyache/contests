import heapq

def last(stones):
    hp = [-x for x in stones]
    heapq.heapify(hp)
    while len(hp) > 1:
        x1 = heapq.heappop(hp)
        x2 = heapq.heappop(hp)
        if x1 != x2:
            heapq.heappush(hp, x1 - x2)

    return -hp[0] if hp else 0

stones = [2,7,4,1,8,1]
print(last(stones))