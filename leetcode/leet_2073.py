from collections import deque

def time(tickets, k):
    q = deque(tickets)
    cnt = 0
    while  q:
        curr = q.popleft() -1
        if k == 0 and curr == 0:
            cnt += 1
            break
        if curr != 0:
            q.append(curr)
        cnt += 1
        k -= 1
        if k == -1:
            k = len(q) -1

    return cnt

tickets = [5,1,1,1]
k = 0
print(time(tickets, k))

