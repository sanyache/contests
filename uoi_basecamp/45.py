import  math

n = int(input())
nums = [int(x) for x in input().split()]
m = int(input())
rez = []
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    max_g = 1
    for i in range(l, r+1):
        g = nums[i]
        for j in range(i+1, r+1):
            g = math.gcd(g, nums[i])
            max_g = max(max_g, g)
    rez.append(max_g)
for val in rez:
    print(val)