n= int(input())
balls = [int(x) for x in input().split()]
counter = 0
s = 0
for ball in balls:
    s+=ball
    if s > n:
        break
    counter += 1
print(counter)
# eolymp 10923