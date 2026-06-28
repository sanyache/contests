import  math

n = int(input())
l_sq = int(math.sqrt(n))
s = 4 + (l_sq-1)*6 + (l_sq-1)**2 * 2
rem = n - l_sq**2
if rem != 0:
    corner = 1
    if rem > l_sq:
        corner += 1
    s += corner*3 + (rem-corner)*2
print(s)