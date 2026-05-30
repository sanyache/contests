def get_basket(fruits, baskets):
    used = [False] *(len(baskets))
    cnt = 0
    for fruit in fruits:
        for ind, basket in enumerate(baskets):
            if not used[ind] and fruit <= basket:
                cnt+= 1
                used[ind] = True
                break
    return len(fruits) - cnt

fruits = [4,2,5]
baskets = [3,5,4]
print(get_basket(fruits, baskets))