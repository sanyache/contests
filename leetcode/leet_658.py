class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        ind = 0
        while ind < n:
            if arr[ind] > x:
                if ind == 0:
                    break
                if arr[ind] - x >= x - arr[ind-1]:
                    ind = ind-1
                    break
                break
            if arr[ind] == x:
                break
            ind += 1
        if ind == n:
            return arr[-k:]
        l = ind
        r = ind
        for _ in range(k-1):
            if l - 1 < 0:
                r += 1
                continue
            if r + 1 == n:
                l -= 1
                continue
            if l-1 >= 0 and r + 1 < n and x - arr[l-1] <= arr[r+1] - x:
                l -= 1
                continue
            if l - 1 >= 0 and r + 1 < n and x - arr[l - 1] > arr[r + 1] - x:
                r += 1
        return arr[l:r+1]
