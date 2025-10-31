s = input()
y = int(s[1])
x = ord(s[0]) - 96
moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
cnt = 0
for dx, dy in moves:
    if 1 <= x + dx <= 8 and 1 <= y + dy <= 8:
        cnt += 1
print(cnt)