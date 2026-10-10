def first_step(n):

    print(n, n-1)
    for i in range(1, n-1):
        print(i, n)
    print(n-1, 1)
    print(n-1, n)
    print(1, n)
    return

def second_step(ind, n):
    if ind == 1:
        return
    print(ind, n)
    for i in range(1, ind):
        print(i, ind)
    print(n, ind)
    second_step(ind-1, n)
n = int(input())
steps= n -1 + (n*(n+1))//2
print(steps)
first_step(n)
second_step(n-1, n)