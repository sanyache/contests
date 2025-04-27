class Solution:
    def isHappy(self, n: int) -> bool:
        map_n = set()
        while not (n in map_n):
            map_n.add(n)
            n = str(n)
            s = 0
            for i in n:
                s += int(i)*int(i)
            n = int(s)
            if n == 1:
                return True
        return False