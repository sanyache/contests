n = int(input())
numbers = [int(x) for x in input()]
prefix_sum = [ 0 for i in range(n+1)]
for i in range(1, n+1):
    prefix_sum[i] = (prefix_sum[i-1] + numbers[i-1])
for i in range(1, n):
    for j in range(i+1, n+1):
        l = prefix_sum[j] -prefix_sum[i-1]
        if l > 1  and (j-i+1) % l == 0:
            print(i, j)
            exit()