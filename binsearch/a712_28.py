"""
eolymp 3969
На якому найменшому квадраті можна розмістити n прямокутників w*h
1<=w,h,n<= 10**9
Input
2 3 10
Output
9
"""
from math import pow
w, h, n = map(int, input().split())
l = 1
r = int(pow(10, 18))
while r>l:
    x = (r+l)//2
    if ((x//w) * (x//h)) >= n:
        r = x
    else:
        l = x+1
print(l)