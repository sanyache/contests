l, r = map(int, input().split())
numbers= [int(x) for x in input().split()]
n = len(numbers)
prefix_sum = [ 0 for i in range(n+1)]
for i in range(1, n+1):
    prefix_sum[i] = (prefix_sum[i-1] + numbers[i-1])
print(prefix_sum)
print(prefix_sum[r] - prefix_sum[l-1])