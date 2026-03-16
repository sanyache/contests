a, b, c = map(int, input().split())
dig = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
if a+b == c:
    print("Yes")
    exit()
have = dig[a] + dig[b]
for i in range((c+1)//2):
    if  dig[i] + dig[c-i] == have:
        print("Yes")
        break
else:
    print("No")