n = int(input())
nums = [int(x) for x in input().split()]

stack = list()
rez = list()
cnt = 1
for num in nums:
    if  rez and rez[-1] > num:
        cnt += 1
        rez = []
        stack = []
    while stack and num > stack[-1]:
        rez.append(stack.pop())
    stack.append(num)

print(cnt)