n = int(input())
lights = [True if x=='G' else False for x in input()]
counter = 0
for light in lights:
    if counter %2 != 0:
        light = not light
    if light:
        counter += 1
    else:
        counter += 2
print(counter)