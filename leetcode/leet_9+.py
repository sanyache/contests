def is_palindrom(x):
    n = len(x)
    for i in range(n//2):
        if x[i] != x[n-1-i]:
            return False
    return True

n = 12621
print(is_palindrom(str(n)))