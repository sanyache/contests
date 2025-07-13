def isSubsequence(self, s: str, t: str) -> bool:
    if s == "" and t != "":
        return True
    if s != "" and t == "":
        return False
    if s == "" and t == "":
        return True
    l = 0
    for i in range(len(t)):
        if t[i] == s[l]:
            l += 1
        if l == len(s):
            return True
    return False