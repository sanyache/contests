def is_correct(s):
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
        if ch == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0
def bin_gen(l, prefix= ""):
    global rez
    if l == 0:
        if is_correct(prefix):
            rez.append(prefix)
    else:
        bin_gen(l-1, prefix + '(')
        bin_gen(l-1, prefix + ')')



n = 3
rez = list()
bin_gen(n*2)
print(rez)