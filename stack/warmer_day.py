"""
Дано список температур у певний день. Визначити для кожного дня
коли настане тепліший день
"""
def warmer_days(temps):
    n = len(temps)
    rez = [0]*n
    stack = list()
    for i in range(n-1, -1, -1):
        while stack and temps[i] > stack[-1][0]:
            stack.pop()
        if stack:
            rez[i] = stack[-1][1] - i
        stack.append((temps[i], i))
    return rez

temps = [13, 12, 15, 11, 9, 12, 16]
print(warmer_days(temps))
