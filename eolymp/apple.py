n, g, y, r = map(int, input().split())

ind_tpm = n%(2*g + 2*y + r)
if 1<= ind_tpm <= g:
    print('G')
elif g < ind_tpm <= (g+y):
    print('Y')
elif (g+y) < ind_tpm <= (g+y+r):
    print('R')
elif (g+y+r) < ind_tpm <= (g + 2*y + r):
    print('Y')
else:
    print('G')