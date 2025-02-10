"""
Дано натуральне число. Використовуючи цифри з нього,
скільки можна згенерувати різних трьоцифрових чисел?
Input:
112222234
Output:
43
"""
from collections import Counter
cnt = 0
def number_permutation(digits, l, prefix=''):
    global cnt
    if l == 0:
        if prefix[0] != '0':
            cnt += 1
            print(prefix)
        return
    for key in digits.keys():
        i = int(key)
        if digits[key] == 0:
            continue
        digits[key] -= 1
        number_permutation(digits, l-1, prefix + str(i))
        digits[key] += 1
row = input()
if len(row) < 3:
    print(0)
    exit()
digits = Counter(row)

number_permutation(digits, 3)
print(cnt)
