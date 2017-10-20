import itertools

x = range(1, 10)
for i, j in itertools.product(x, x):
    print(str(i)+' x '+str(j)+' = '+str(i*j))