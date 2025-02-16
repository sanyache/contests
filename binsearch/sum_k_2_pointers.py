"""
Дано відсортований масив, вивести  пару чисел, яка в сумі дає k
Input:
3
-9 -5 -2 -1 1 4 9 11
Output:
-1 4
"""
k = int(input())
numbers = [int(x) for x in input().split()]
l = 0
r = len(numbers) -1
while r > l:
    s = numbers[l] + numbers[r]
    if s == k:
        print(numbers[l], numbers[r])
        exit()
    if s > k:
        r -= 1
    else:
        l += 1
print("No solution")

