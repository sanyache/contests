from collections import Counter

s = input()
s_map = dict()
for i in s:
    if s_map.get(i):
        s_map[i] += 1
    else:
        s_map[i] = 1
print(s_map)
print(Counter(s))