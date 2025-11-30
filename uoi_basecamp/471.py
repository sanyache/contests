import math
n, x, s, y = map(int, input().split())
rest = x - n - s*y
if rest > 0:
    print(math.ceil(rest/s))
else:
    print(0)
