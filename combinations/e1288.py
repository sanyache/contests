n,a,b = map(int, input().split())
if a == 0 and b == 0:
    print(0)
elif a == b or a*b == 0:
    rez = '1' + '0'*(n-1)
    print(rez)
else:
    rez = '2' + '0'*(n-1)
    print(rez)