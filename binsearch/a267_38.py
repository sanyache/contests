"""
Працюють 2 ксерокси. В одного швидкість x копій за секунду, в іншого y. Потрібно
зробити n копій. Який мінімальний час потрібен?
Input:
4 1 1
Output:
3
Input:
5 1 2
Output:
4
"""
n, x, y = map(int, input().split())
if x > y:
    x,y = y,x
if n == 1:
    print(x)
    exit()
n -= 1
l = x
r = n*y
while r > l:
    mid = (r+l)//2
    if (mid//x + mid//y) >= n:
        r = mid
    else:
        l = mid + 1
print(l + x)