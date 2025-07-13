def search(arr):
    left, right = 0, len(arr) - 1

    while right - left > 2:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3
        if arr[m1] < arr[m2]:
            left = m1
        else:
            right = m2

    # Перевіримо вручну на максимум в межах [left, right]
    peak = left
    for i in range(left + 1, right + 1):
        if arr[i] > arr[peak]:
            peak = i
    return peak


nums = [20, 23, 34, 56, 78, 90, 98, 73, 67, 12, 7]
print(search(nums))