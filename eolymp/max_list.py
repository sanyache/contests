n = int(input())
numbers = [int(x) for x in input().split()]
a = [0] * (n+1)
a[0] = numbers[0]
a[1] = numbers[0]
for i in range(1, n):
    a[i] = min(numbers[i], a[i])
    a[i+1] = max(a[i], numbers[i])
print(*a)
print(sum(a))