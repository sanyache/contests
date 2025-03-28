"""
Визначити розмір найдовшої послідовності, яка не містить однакових символів.
"""
s = input()
l = 0
s_map = set()
max_l = 0
for r in range(len(s)):
    while s[r] in s_map:
        s_map.remove(s[l])
        l += 1
    s_map.add(s[r])
    max_l = max(max_l, len(s_map))
print(max_l)