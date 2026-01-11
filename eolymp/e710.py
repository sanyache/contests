def normalize(rect):
    x1, y1, x2, y2 = rect
    return (
        min(x1, x2),  # left
        max(x1, x2),  # right
        min(y1, y2),  # bottom
        max(y1, y2)   # top
    )


n = int(input())
rects = [normalize(tuple(map(int, input().split()))) for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (
            rects[j][0] <= rects[i][0] and
            rects[j][1] >= rects[i][1] and
            rects[j][2] <= rects[i][2] and
            rects[j][3] >= rects[i][3]
        ):
            is_outer = False
            break
    else:
        cnt += 1

print(cnt)

