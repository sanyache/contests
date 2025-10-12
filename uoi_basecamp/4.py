b = sum([int(x) for x in input().split()])
m = sum([int(x) for x in input().split()])
t = sum([int(x) for x in input().split()])
rez = min(b, m ,t)
if b == rez:
    print("Bus")
elif m == rez:
    print("Metro")
else:
    print("Taxi")
