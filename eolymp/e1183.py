import sys
import math
def is_bin(n):
    return bin(n)[2:].count('1') == 1


data = []
rez = []
for line in sys.stdin:
    a, b = map(int, line.split())
    data.append((a,b))
for a, b in data:
    if a + b < 1 or not is_bin((a+b)//math.gcd(a,b)):
        rez.append(-1)
        continue
    cnt = 0
    while a > 0 and b > 0:
        if a > b:
            a = a- b
            b *= 2
        else:
            b = b - a
            a *= 2

        cnt += 1
    rez.append(cnt)
for cnt in rez:
    print(cnt)
