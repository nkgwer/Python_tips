def double(x):
    return 2*x


cin = 10

print(double(cin))

f = lambda x: 2*x

# It works but don't assign a lambda expression, use def

print(f(10))

list_ = range(10)

list_ = list(map(lambda x: x*2, list_))

print(list_)

