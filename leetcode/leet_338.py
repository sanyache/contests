
def countBits(n):
    d = [0]*(n+1)
    pow = 1
    for i in range(1,n+1):
        if i == pow*2:
            d[i] = 1
            pow *= 2
        else:
            d[i] = 1 + d[i-pow]
    return d

n = 8
print(countBits(n))