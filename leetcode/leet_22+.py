
def bin_gen(l, left, right, prefix):
    if left > n or left < right:
        return
    if l == 0:
        cnt = 0
        rez.append(prefix)
    else:
        bin_gen(l-1, left+1, right, prefix + '(')
        bin_gen(l-1, left, right + 1, prefix + ')')


n = 3
rez = list()
a=0
b = 0
bin_gen(n*2, a, b, "")
print(rez)