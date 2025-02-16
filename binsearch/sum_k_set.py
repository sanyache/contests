"""
Дано відсортований масив, вивести  пару чисел, яка в сумі дають k
Input:
3
-9 -5 -2 -1 1 4 9 11
Output:
-1 4
"""
k = int(input())
numbers = [int(x) for x in input().split()]
set_num = {x for x in numbers}
for number in numbers:
    if k-number in set_num:
        print(number, k-number)
        exit()
print('No solution')