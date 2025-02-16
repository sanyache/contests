def search(data1, data2):
    ind1 = len(data1)-1
    ind2 = len(data2)-1
    while ind1 >= 0 and ind2 >= 0:
        if data1[ind1] == data2[ind2]:
            return data1[ind1]
        if data1[ind1] > data2[ind2]:
            ind1 -= 1
        else:
            ind2 -= 1
    return -1

row1 = [int(x) for x in input().split()]
n = row1[0]
if n == 0:
    print(-1)
    exit()
row2 = [int(x) for x in input().split()]
m = row2[0]
if m == 0:
    print(-1)
    exit()
print(search(row1[1:], row2[1:]))

