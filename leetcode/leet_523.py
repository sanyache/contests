def check(nums, k):
    prefix_mod = dict()
    prefix_mod[nums[0]%k] = 0
    s = nums[0]
    for i in range(1,len(nums)):
        s += nums[i]
        if s%k == 0:
            return True
        if s%k in prefix_mod and  i - prefix_mod[s%k] > 1 :
            return True
        if not s%k in prefix_mod:
            prefix_mod[s%k] = i
    return False

nums = [1,2, 3]
k = 5
print(check(nums, k))
