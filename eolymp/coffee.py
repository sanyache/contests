age = int(input())
son, father, = map(int, input().split())
if age < 18:
    if father > 1 :
        print('Yes')
    else:
        print('No')
else:
    if son > 1:
        print('Yes')
    else:
        print('No')