class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        rez = list()
        map_lists = dict()
        for key in set(nums1):
            if key in map_lists:
                map_lists[key] += 1
            else:
                map_lists[key] = 1
        for key in set(nums2):
            if key in map_lists:
                map_lists[key] += 1
            else:
                map_lists[key] = 1
        for key in set(nums3):
            if key in map_lists:
                map_lists[key] += 1
            else:
                map_lists[key] = 1
        for key, val in map_lists.items():
            if val > 1:
                rez.append(key)
        return rez