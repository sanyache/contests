s = input()
R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
n = R[s[len(s)-1]]
tmp = R[s[len(s)-1]]
stack = 0
for i in range(len(s)-2, -1, -1):
     if R[s[i]] < tmp:
         n -= R[s[i]]
     elif R[s[i]] == tmp:
         stack += R[s[i]]
     else:
         n += R[s[i]] + stack
         stack = 0
         tmp = R[s[i]]

if stack:
    n += stack
print(n)
