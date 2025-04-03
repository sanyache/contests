def pref(strs):

    min_s = min([len(x) for x in strs])
    longest = ""
    for i in range(min_s):
        tmp = strs[0][i]
        for word in strs:
            if word[i] != tmp:
                return longest
        else:
            longest += tmp
    return longest

s = ["flower","flow","flight"]
print(pref(s))