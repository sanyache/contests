n, q, x = map(int, input().split())

teams = dict()
max_time = 0
for i in range(q):
    time, team = map(int, input().split())
    max_time = max(max_time, time)
    if team in teams:
        teams[team].append(time)
    else:
        teams[team] = [time]

rez = list()
for team, times in teams.items():
    times.sort()
    for i in range(len(times)):
        if i % 2 != 0 and times[i] - times[i - 1] > x:
            rez.append(team)
            break
    if i % 2 == 0 and max_time - times[i] > x:
        rez.append(team)

print(len(rez))
rez.sort()
print(*rez)
