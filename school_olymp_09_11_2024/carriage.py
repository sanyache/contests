carriage = list()
cell = list()
for i in range(1,37):
    cell.append(i)
    if i % 4 == 0:
        cell.append((9 - i//4) * 2 + 36 + 1)
        cell.append((9 - i // 4) * 2 + 36 + 2)
        carriage.append(cell)
        cell = []
carriage = [set(row) for row in carriage]
n = int(input())
for _ in range(n):
    place = int(input())
    for row in carriage:
        if place in row:
            row.remove(place)
            continue
counter = 0
max_counter = 0
for row in carriage:
    if not row:
        counter +=1
    else:
        counter = 0
    if counter > max_counter:
        max_counter = counter
print(max_counter)