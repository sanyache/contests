n = input()
n1 = int(n[:2])
n2 = int(n[2:])
if n1 %3  == 0 and n2%3 == 0:
    print('Yes')
else:
    print('No')
if n1 %5  == 0 and n2%5 == 0:
    print('Yes')
else:
    print('No')
if n1 %7  == 0 and n2%7 == 0:
    print('Yes')
else:
    print('No')