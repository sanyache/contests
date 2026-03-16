from math import isqrt

def check(a, b):
    if a == 0 :
        return 0, 0
    k = b//a
    prev = check(b%a, a)
    if k%2 == 1:
        prev = prev[1], prev[0]
    return prev[0] + a*a*((k+1)//2), prev[1] + a*a*(k//2)
def simple_check(n, m, p, q):
    if n == 0 or m == 0:
        return
    if n> m :
        n,m = m, n
    m -= n
    p += n*n
    simple_check(n, m, q, p)

p, q = map(int, input().split())
s = p + q
div = []


for i in range(1, isqrt(p)+1):
    if s%i == 0:
        div.append(i)
for div1 in div:
    div2 = s// div1
    r1, r2 = check(div2, div1)
    print(div1, div2, r1, r2)
    if r1  == p and r2 == q:
        print(div1, div2)
        break
else:
    print(-1)

