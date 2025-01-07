n = int(input())
s = input()
first = s.find('1')
second = s.find('1', first+1)
if second - first == 1:
    print(first+1, second+1)
    exit()
if (second - first + 1) % 2 == 0:
    print(first+1, second+1)
elif first != 0:
    print(first, second+1)
elif s[second+1] == '0':
    print(first+1, second+2)
else:
    print(second+1, second+2)
