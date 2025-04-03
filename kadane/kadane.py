"""
Знайти максимальну суму підмасиву
-1  2 4 -3 5 2 -5 2
10

"""
numbers = [int(x) for x in input().split()]
n = len(numbers)
best = numbers[0]
curr_sum = 0
for i in range(n):
    curr_sum = max(curr_sum+numbers[i], numbers[i])
    best = max(best, curr_sum)
print(best)