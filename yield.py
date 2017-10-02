def f1():
    yield 1
    yield 2
    yield 3


for i in f1():
    print(i)


def f2():
    x = 0
    while x < 10:
        yield x
        x += 1

        
for i in f2():
    print(i)