def maxProfit(nums):
    best = 0
    min_cost = nums[0]
    for num in nums:
        min_cost = min(min_cost, num)
        best = max(best, num - min_cost)
    return best


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))