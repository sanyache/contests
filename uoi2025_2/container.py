a, b, c = map(int, input().split())
if (a + b + c) % 3 !=0:
    print('-1')
else:
    mid = (a+b+c)//3
    counter = abs(a-mid) + abs(b-mid) + abs(c-mid)
    print(counter/2)