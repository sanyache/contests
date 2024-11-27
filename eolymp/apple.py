n, g, y, r = map(int, input().split())
template = 'G'*g + 'Y'*y + 'R'*r + 'Y'*y + 'G'*g
ind_tpm = (n-1)%len(template)
print(template[ind_tpm])