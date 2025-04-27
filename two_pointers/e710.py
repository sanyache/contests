def areOccurrencesEqual(s: str) -> bool:
    map_s = dict()
    for ch in s:
        if map_s.get(ch):
            map_s[ch] += 1
        else:
            map_s[ch] = 1
    flag = map_s[s[0]]
    for val in map_s.values():
        if val != flag:
            return False

    return  True
s = "abacbc"
print(areOccurrencesEqual(s))