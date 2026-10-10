n = int(input())
nums = [int(x) for x in  input().split()]
m_s = dict()
for val in nums:
    if val in m_s:
        m_s[val] += 1
    else:
        m_s[val] = 1
colors = sorted(m_s.items(), key=lambda x: -x[1])
c = max(m_s.items(), key=lambda x: x[1])[1]
best = n
for color, val in colors[:10]:
    s = nums.copy()
    # if val < c:
    #     break
    cnt = 0
    for i in range(n-1):
        if s[i] !=color and s[i+1] != color:
            s[i] = color
            s[i+1] = color
            cnt += 1
    for i in range(n):
        if s[i] != color:
            cnt += 1

    best = min(best, cnt)
print(best)