a, b, x, y = map(int, input().split())
rez = (a-x + (b-y)*2)/(a + b*2)
print("YES" if rez > 0.505 else "No")