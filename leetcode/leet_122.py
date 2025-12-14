def maxProfit(prices) -> int:
    n = len(prices)
    s = 0
    stack = list()
    stack.append(prices[-1])
    for i in range(n - 2, -1, -1):
        while stack and prices[i] > stack[-1]:
            stack.pop()
        stack.append(prices[i])
        if len(stack) > 1:
            s += stack[0] - stack[-1]
            stack = [stack[-1]]

    return s

prices = [7,1,5,3,6,4]
print(maxProfit(prices))