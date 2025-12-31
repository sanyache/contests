import heapq


def getOrder(tasks):
    n = len(tasks)
    for i in range(n):
        tasks[i].append(i)
    tasks.sort(key=lambda x: x[0])
    pq = []
    i = 0
    finish = tasks[0][0]
    rez = []
    while i < n or pq:

        while i < n and tasks[i][0] <= finish:
            heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
            i += 1
        if pq:
            time, ind = heapq.heappop(pq)
            finish += time
            rez.append(ind)
        elif i < n:
            finish = tasks[i][0]
    return rez

tasks = [[1,2],[2,4],[3,2],[4,1]]

print(getOrder(tasks))