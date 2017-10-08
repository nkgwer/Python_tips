from collections import  defaultdict

colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d1 = {}
for color in colors:
    if color not in d1:
        d1[color] = 0
    d1[color] += 1

d2 = {}
for color in colors:
    d2[color] = d2.get(color, 0) + 1

d3 = defaultdict(int)
for color in colors:
    d3[color] += 1

print(d1)
print(d2)
print(d3)
print(dict(d3))

