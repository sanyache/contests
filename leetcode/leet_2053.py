class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map_arr = dict()
        for val in arr:
            if map_arr.get(val):
                map_arr[val] += 1
            else:
                map_arr[val] = 1
        cnt  = 0
        for val in arr:
            if map_arr[val] == 1:
                cnt += 1
            if cnt == k:
                return val
        return ""