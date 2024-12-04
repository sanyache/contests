from math import pow, ceil, log2

def resize(arr):
    n = int(pow(2, ceil(log2(len(arr)))))
    arr.extend([0]*(n-len(arr)))

class SegTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.s_tree = [0]*2* self.n
        self.__bild_tree(0,0, self.n)

    def __bild_tree(self,start, left, right):
        if left == right-1:
            self.s_tree[start] = self.arr[left]
        else:
            mid = (left+right)//2
            self.__bild_tree(start*2+1, left, mid)
            self.__bild_tree(start*2+2, mid, right)
            self.s_tree[start] = self.s_tree[start*2 + 1]+ self.s_tree[start*2+2]

    def update(self, ind, val):
        self.__update(ind, val, 0, 0, self.n)

    def __update(self, ind, val, node, left, right):
        if left == right -1:
            self.s_tree[node] = val
            return
        mid = (left + right)//2
        if ind < mid:
            self.__update(ind, val, 2*node+1, left, mid)
        else:
            self.__update(ind, val, 2*node+2, mid, right)
        self.s_tree[node] = self.s_tree[2*node+1] + self.s_tree[2*node+2]

    def sum(self, left, right):
        return self.__sum(left, right, 0, 0, self.n)

    def __sum(self, left, right, node, l_seg, r_seg):
        if right <= l_seg or left >= r_seg:
            return 0
        if l_seg >= left and r_seg <= right:
            return self.s_tree[node]
        mid = (l_seg + r_seg)//2
        sum_ = self.__sum(left, right, 2*node+1, l_seg, mid) + self.__sum(left, right, 2*node+2, mid, r_seg)

        return sum_

    def get_seg_tree(self):
        return self.s_tree


numbers = [int(x) for x in input().split()]
resize(numbers)
print(numbers)
seg_tree = SegTree(numbers)
print(seg_tree.get_seg_tree())
#seg_tree.update(4, 1)
#print(seg_tree.get_seg_tree())
print(seg_tree.sum(1, len(numbers)))