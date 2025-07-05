def nextGreaterElement(nums1, nums2):
    n = len(nums2)
    greater = dict()
    stack = list()
    ans = list()
    for i in range(n-1, -1, -1):
        while stack and nums2[i] > stack[-1]:
            stack.pop()
        if stack:
            greater[nums2[i]] = stack[-1]
        else:
            greater[nums2[i]] = -1
        stack.append(nums2[i])
    for val in nums1:
        ans.append(greater[val])
    return ans

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))
