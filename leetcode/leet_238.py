def product(nums):
    n = len(nums)
    rez = [0]*n
    pref = [1]*(n+1)
    suf = [1]*(n+1)
    for i in range(1,n+1):
        pref[i] = pref[i-1] * nums[i-1]
    for i in range(n-1, -1, -1):
        suf[i] = suf[i+1] * nums[i]
    for i in range(n):
        rez[i] = pref[i] * suf[i+1]
    return rez

nums = [1,2,3,4]
print(product(nums))