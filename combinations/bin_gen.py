"""
Generate all binary strings of length n
"""
def bin_gen(l, prefix = ''):
    if l == 0:
        print(prefix)
    else:
        bin_gen(l-1, prefix + '0')
        bin_gen(l-1, prefix + '1')


len_comb = int(input())
bin_gen(len_comb)