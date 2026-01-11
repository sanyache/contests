def low_point(n, start, x):
    h = [start] * n
    h[1] = x
    for i in range(2, n):
        h[i] = 2 * h[i - 1] - h[i - 2] + 2
    return min(h), h[-1]


values = input().split()
n = int(values[0])
start = float(values[1])
l = 0
r = 1000000
while r - l >= 0.0000001:
    mid = (r + l) / 2
    low, last = low_point(n, start, mid)
    if low < 0:
        l = mid
    else:
        r = mid
print(f'{last:.02f}')


