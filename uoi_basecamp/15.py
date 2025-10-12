n = int(input())
rez = []
for _ in range(n):
    nums = [int(x) for x in input().split()]
    nums.sort()
    for i in range(12):
        if nums[i] != nums[4*(i//4)]:
            rez.append('no')
            break
    else:
        rez.append('yes')
for val in rez:
    print(val)
