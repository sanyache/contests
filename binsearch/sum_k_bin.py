"""
Дано відсортований масив, вивести  пару чисел, яка в сумі дають k
Input:
3
-9 -5 -2 -1 1 4 9 11
Output:
-1 4
"""
def bin_search(A, val):
    l = 0
    r = len(numbers)-1
    while r >= l:
        mid = (r+l)//2
        if A[mid] == val:
            return mid
        if A[mid] > val:
            r = mid - 1
        else:
            l = mid + 1
    return -1


k = int(input())
numbers = [int(x) for x in input().split()]
for number in numbers:
    if bin_search(numbers, k-number) != -1:
        print(number, k-number)
        exit()
print("Element not found")