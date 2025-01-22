cnt = 0
def read_prefix(prefix):
    lowercase_letters = [chr(i) for i in range(97, 123)]  # ASCII коди від 'a' до 'z'
    rez = ''
    for dig in prefix:
        rez += lowercase_letters[int(dig)]
    print(rez)
    exit()


def gen_comb(l, ind, used, prefix = ''):
    global cnt
    if l == 0:
        print(prefix)
        cnt += 1
        if cnt == ind:
            read_prefix(prefix)
        return
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        gen_comb(l-1, ind,used,  prefix + str(i))
        used[i] = False


n, k = map(int, input().split())
used = [False]*n

gen_comb(n, k, used)
