def left_boundary(sub, targ):
    l = 0
    r = len(sub)
    while l < r:
        med = (r+l)//2
        if sub[med] < targ:
            l = med +1
        else:
            r = med
    return l
def len_sub(nums):
    n = len(nums)
    sub = [nums[0]]
    for i in range(1, n):
        if nums[i] > sub[-1]:
            sub.append(nums[i])
        else:
            ind = left_boundary(sub, nums[i])
            sub[ind] = nums[i]
    return len(sub)

nums = [10,9,2,5,3,7,101,18]
print(len_sub(nums))

"""
Насправді, цей відсортований масив — не підпослідовність.
Тут ми зберігаємо для кожної довжини підпослідовності мінімальний елемент,
у якому вона може закінчуватися.
"""