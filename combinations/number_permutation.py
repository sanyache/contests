import math

def number_permutation(n, l, prefix='', used=None):
    used = used or [False]*(n+1)
    if l == 0:
        print(prefix)
        return
    for i in range(1, n+1):
        if used[i]:
            continue
        used[i] = True
        number_permutation(n, l-1, prefix + str(i), used)
        used[i] = False


number, length = map(int, input().split())
number_permutation(number, length)
permutations = math.perm(number, length)
print(permutations)
