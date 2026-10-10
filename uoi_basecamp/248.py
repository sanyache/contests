boxes = []
s_y = 0
s_b = 0
for i in range(3):
    y, b = map(int, input().split())
    s_y += y
    s_b += b
    boxes.append((y,b))
best = s_y + s_b
cnt_y = 0
cnt_b = 0
for i in range(3):
    cnt_y = s_y - boxes[i][0]
    for j in range(1,3):
        ind = (i+j)%3
        cnt_b += boxes[ind][1]
        best = min(best, cnt_y + boxes[i][1] + boxes[ind][1])
print(best)

