from collections import Counter
k = int(input())
rez = []
for _ in range(k):
    n = int(input())
    nums = [int(x) for x in input()]
    for l in range(n):
        is_break = False
        for r in range(l+1, n):
            map_nums = Counter(nums[l: r+1])
            if len(map_nums) *2 <= r-l +1:
                is_break = True
                break
        if is_break:
            rez.append("No")
            break
    else:
        rez.append("Yes")
for val in rez:
    print(val)