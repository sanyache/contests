
def fix_arr(arr, _s, target):
    if target > _s:
        arr.sort()
        return True
    if target < 0:
        arr.sort(reverse=True)
        return True
    # 0 < x < sum
    arr.sort(reverse=True)
    pref = 0
    to_fix = False
    for i in range(len(arr)):
        pref += arr[i]
        if pref == target:
            to_fix = True
        if pref>target:
            break
    if not to_fix:
        return True
    it_for_x = i-1
    it = i
    if arr[0] != arr[it]:
        arr[0], arr[it] = arr[it], arr[0]
        return True

    while (it< len(arr)
           and (
                abs(arr[it_for_x]) == abs(arr[it])
                or arr[it] == 0
                or abs(arr[it])%arr[it_for_x]==0
           )
    ):
        it += 1
    if it == len(arr):
        return False
    else:
        arr[it_for_x], arr[it] = arr[it], arr[it_for_x]
    return True

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = []
    s = 0
    row = input()
    for item in row.split():
        val = int(item)
        a.append(val)
        s += val
    if s == x:
        print("NO")
        continue
    is_inverse = False
    if s<0:
        is_inverse = True
        for i in range(n):
            a[i] *= -1
        s = -s
        x = -x
    is_fixed = fix_arr(a, s, x)
    if is_fixed:
        print("YES")
        if is_inverse:
            a = [-1*x for x in a]
        print(*a)
    else:
        print("NO")

