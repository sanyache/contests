def topKFrequent(nums ,k):
    map_nums = dict()
    for num in nums:
        if num in map_nums:
            map_nums[num] += 1
        else:
            map_nums[num] = 1

    sort_pair = sorted(map_nums.items(), key=lambda x: -x[1])
    rez = []
    for key, val in sort_pair[:k]:
        rez.append(key)
    return rez

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))