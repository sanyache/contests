class Solution:
    def checkAlmostEquivalent(self, s1: str, s2: str) -> bool:
        map_s1 = dict()
        map_s2 = dict()
        for val in s1:
            if map_s1.get(val):
                map_s1[val] += 1
            else:
                map_s1[val] = 1
        for val in s2:
            if map_s2.get(val):
                map_s2[val] += 1
            else:
                map_s2[val] = 1
        for key in map_s1.keys():
            if abs(map_s1[key] - map_s2.get(key, 0)) > 3:
                return False
        for key in map_s2.keys():
            if abs(map_s2[key] - map_s1.get(key, 0)) > 3:
                return False

        return True