import sys
from collections import deque


def main():
    stream = sys.stdin.buffer
    h, w, n = map(int, stream.readline().split())
    s = stream.readline().decode().strip()

    if s.count('L') < w-1 and s.count('R') < w-1 or s.count('U') < h-1 and s.count('D') < h-1:
        print(-1)
        return

    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    for i in range(n):
        X[i+1] = X[i] + (1 if s[i] == 'R' else -1 if s[i] == 'L' else 0)
        Y[i+1] = Y[i] + (1 if s[i] == 'D' else -1 if s[i] == 'U' else 0)

    maxX, minX, maxY, minY = deque(), deque(), deque(), deque()

    best = n + 1
    l = 0

    maxX.append(0); minX.append(0); maxY.append(0); minY.append(0)

    for r in range(n):
        i = r + 1
        while maxX and X[maxX[-1]] <= X[i]: maxX.pop()
        maxX.append(i)
        while minX and X[minX[-1]] >= X[i]: minX.pop()
        minX.append(i)
        while maxY and Y[maxY[-1]] <= Y[i]: maxY.pop()
        maxY.append(i)
        while minY and Y[minY[-1]] >= Y[i]: minY.pop()
        minY.append(i)


        while l < r and X[maxX[0]] - X[minX[0]] >= w-1 and Y[maxY[0]] - Y[minY[0]] >= h-1:
            best = min(best, r - l + 1)
            l += 1
            while maxX and maxX[0] < l: maxX.popleft()
            while minX and minX[0] < l: minX.popleft()
            while maxY and maxY[0] < l: maxY.popleft()
            while minY and minY[0] < l: minY.popleft()

    print(best if best <= n else -1)


if __name__ == "__main__":
    main()