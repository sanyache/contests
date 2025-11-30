n = int(input())
s = input()
s += s
l = 0
best = 0
for r in range(1, 2*n):
    if ord(s[r]) - ord(s[r-1]) == 1:
        best = max(best, r-l + 1)
    else:
        l = r
print(best)

