def is_in_list(check_set, data):
    for i in range(len(data)-1, -1, -1):
        if data[i] in check_set:
            return data[i]
    return -1
row1 = input()
if row1[0] == '0':
    print(-1)
    exit()
row2 = input()
if row2[0] == '0':
    print(-1)
    exit()
n, data1 = row1.split(' ', 1)
set_data1 = {int(x) for x in data1.split()}
m, data2 = row2.split(' ', maxsplit=1)
d2 = [int(x) for x in data2.split()]
print(is_in_list(set_data1, d2))