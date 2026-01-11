import math
import sys

data = []
rez = []
for line in sys.stdin:
    x = int(line)
    data.append(x)
for val in data:
    if val == 0:
        rez.append(0)
        continue
    curr = math.log(val, 3)
    rez.append(math.ceil(curr))
for val in rez:
    print(val)