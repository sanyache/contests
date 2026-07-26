
w = list(map(int, input().split()))

box = list(map(int, input().split()))

sum1 = 0
sum2 = 0

for i in range(4):
    if box[i] == 1:
        sum1 += w[i]
    else:
        sum2 += w[i]

initial_max = max(sum1, sum2)

best_item = -1
best_max = initial_max

for i in range(4):
    if box[i] == 1:
        new1 = sum1 - w[i]
        new2 = sum2 + w[i]
    else:
        new1 = sum1 + w[i]
        new2 = sum2 - w[i]

    cur_max = max(new1, new2)

    if cur_max < best_max:
        best_max = cur_max
        best_item = i + 1

print(best_item)