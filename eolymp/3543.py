
wk, q, bk = input().split()

x1 = ord(q[0]) - ord('a')
y1 = int(q[1])

x2 = ord(bk[0]) - ord('a')
y2 = int(bk[1])

x3 = ord(wk[0]) - ord('a')
y3 = int(wk[1])

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    if x1 == x2 == x3:
        if min(y1, y2) < y3 < max(y1, y2):
            print("NO")
        else:
            print("YES")
    elif y1 == y2 == y3:
        if min(x1, x2) < x3 < max(x1, x2):
            print("NO")
        else:
            print("YES")
    elif abs(x1 - x2) == abs(y1 - y2):
        if abs(x1 - x3) == abs(y1 - y3):
            if min(x1, x2) < x3 < max(x1, x2):
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
    else:
        print("YES")
else:
    print("NO")

