def is_sort(n1):
    nums = [int(x) for x in n1]
    for i in range(len(n1)-1):
        if nums[i] >= nums[i+1]:
            return False
    return True
n = int(input())
while not is_sort(str(n)):
    n += 1
print(n)