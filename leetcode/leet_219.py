class Solution:
    def containsNearbyDuplicate(self, a: List[int], k: int) -> bool:
        if k == 0:
            return False
        k = min(k, len(a))
        map_a = set(a[:k])
        if len(map_a) < k:
            return True
        l = 0
        for i in range(min(k,len(a)), len(a)):
            if a[i] in map_a:
                return True
            map_a.remove(a[l])
            l += 1
            map_a.add(a[i])
        return False
