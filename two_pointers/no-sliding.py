"""
[4, 2, 2, 1, 2, -3, 5, -8] Знайти кількість підмасивів, сума
яких дор k=5
"""
def sum_subarray(nums, k):
    cnt = 0
    prefix_cnt = {0 : 1}
    prefix_sum = 0
    for num in nums:
        prefix_sum += num
        to_remove = prefix_sum - k
        if prefix_cnt.get(to_remove):
            cnt += prefix_cnt.get(to_remove)
        if prefix_cnt.get(prefix_sum):
            prefix_cnt[prefix_sum] += 1
        else:
            prefix_cnt[prefix_sum] = 1
        print(prefix_cnt)
    return cnt


nums = [4,2,2,1,2,-3,5,-8]
k = 5
print(sum_subarray(nums, k))
