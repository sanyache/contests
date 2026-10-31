import sys
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[:2]
    A = data[2:]

    answer = 0
    delta = [0]* (n+1)
    pref = [0]*(n+2)
    suf = [0]*(n+2)
    for i in range(1,n):
        delta[i] = A[i] - A[i-1]
    for i in range(1, n):
        pref[i] = gcd(pref[i-1], delta[i])
    for i in range(n-1, 0, -1):
        suf[i] = gcd(suf[i+1], delta[i])

    for l in range(n-k+1):
        r = l + k -1
        if l < 1:
            l_pref = 0
            mid = 0
            r_suf = suf[r+2]
        elif r+1 > n-1:
            l_pref = pref[l-1]
            mid = 0
            r_suf =0
        else:
            l_pref = pref[l-1]
            mid = A[r+1] - A[l-1]
            r_suf = suf[r+2]
        answer = max(answer, gcd(r_suf, l_pref, mid))
    print(answer)


if __name__ == "__main__":
    main()