a, b, c, d, n, x, y  = map(int, input().split())
apple = a + c
pear = b + d

if apple // n >= x and pear // n >= y:
    print('Yes')
else:
    print('No')