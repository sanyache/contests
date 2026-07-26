d1, m1 = map(int, input().split())
d2, m2 = map(int, input().split())
d1 += 13
if d1 > 30:
    d1 -= 30
    m1 += 1
    if m1 > 12:
        m1 = 1
if d1 == d2 and m1 == m2:
    print("Same birthday!")
else:
    print("Not the same")