n = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()
rez = []
for i in range(n//2):
    rez.append(numbers[i])
    rez.append(numbers[-1-i])
if n%2 != 0:
    rez.append(numbers[n//2])
print(*rez)