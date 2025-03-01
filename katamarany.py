"""
UOI 2025. III stage. Day 2
Катамаран витримує 100кг. Є набір людей із вагою строго
20, 40, 60, 80Є 100 Скільки необхідно катамаранів
для перевезення людей
"""
import math
n = int(input())
numbers = [int(x) for x in input().split()]
nm = {20: 0, 40:0, 60:0, 80:0, 100:0}
for num in numbers:
    nm[num] += 1
cnt = nm[100] + nm[80] + nm[60]
nm[20] -= min(nm[20], nm[80])
min_pair = min(nm[40], nm[60])
nm[40] -= min_pair
nm[60] -= min_pair
nm[20] = max(0, nm[20] - nm[60]*2)
cnt += nm[40]//2
nm[20] = max(0, nm[20]- nm[40]//2)
nm[40] = nm[40]%2
if nm[20] != 0 or nm[40]!= 0:
    cnt += math.ceil((nm[20]*20 + nm[40]*40)/100)
print(cnt)
