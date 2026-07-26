n, m = map(int, input().split())
s = input().split()
sizes = {key: val for val, key in enumerate(s)}
stor = [[int(x) for x in input().split()] for _ in range(n)]
req = [[0]*m for _ in range(n)]
k = int(input())
for _ in range(k):
    data = input().split()
    color = int(data[0])-1
    size = sizes[data[1]]
    if stor[color][size] != 0:
        stor[color][size] -= 1
        continue
    for j in range(size, m):
        is_found = False
        if stor[color][j] !=0:
            stor[color][j] -=1
            break
        for i in range(n):
            if stor[i][j] != 0:
                stor[i][j] -= 1
                is_found = True
                break
        if is_found:
            break
    else:
        req[color][size] += 1
for row in stor:
    print(*row)
for row in req:
    print(*row)

