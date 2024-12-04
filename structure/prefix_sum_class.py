
class PrefixSum:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.prefix = [0 for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            self.prefix[i] = self.prefix[i-1] + self.arr[i-1]

    def sum_pref(self, left, right):
        return self.prefix[right] - self.prefix[left-1]


l, r = map(int, input().split())
numbers = [int(x) for x in input().split()]
prefix_sum = PrefixSum(numbers)
print(prefix_sum.sum_pref(l, r))

