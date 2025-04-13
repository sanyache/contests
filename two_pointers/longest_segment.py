"""
sliding window визначити довжину найдовшого відрізку невід'ємних чисел,
сума елементів якого не перевищує s
"""
s = int(input())
nums = [int(x) for x in input().split()]
l = 0
cur_sum = 0
max_l = 0
for r in range(len(nums)):
    cur_sum += nums[r]
    while cur_sum > s:
        cur_sum -= nums[l]
        l += 1
    max_l = max(max_l, (r-l+1))
print(max_l)
