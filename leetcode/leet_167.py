class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        rez = list()
        while r > l:
            s = numbers[l] + numbers[r]
            if s == target:
                rez.append(l+1)
                rez.append(r+1)
                break
            elif s > target:
                r -= 1
            else:
                l += 1
        return rez