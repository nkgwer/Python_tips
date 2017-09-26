# As the name suggests, filter creates a list of elements for which a function returns true.

l = range(10)

print(list(filter(lambda x: x % 2, l)))

print(list(filter(lambda x: x > 4, l)))
