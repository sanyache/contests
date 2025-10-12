s = [x for x in input()]
for i in range(len(s)):
    if s[i].isupper():
        s[i] = s[i].casefold()
    else:
        s[i] = s[i].capitalize()

print("".join(s))