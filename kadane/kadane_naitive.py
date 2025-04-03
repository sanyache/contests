"""
Знайти максимальну суму підмасиву
-1  2 4 -3 5 2 -5 2
10

"""
numbers = [int(x) for x in input().split()]
n = len(numbers)
best = numbers[0]
for l in range(n):
    curr_sum = 0
    for r in range(l, n):
        curr_sum += numbers[r]
        best = max(best, curr_sum)
print(best)