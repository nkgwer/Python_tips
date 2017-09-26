from functools import reduce
# Reduce is a really useful function for performing some computation on a list and returning the result.
# It applies a rolling computation to sequential pairs of values in a list.

product1 = 1
list_in = [1, 2, 3, 4]
for num in list_in:
    product1 = product1 * num
print(product1)

product2 = reduce((lambda x, y: x * y), list_in)
print(product2)

example = range(1, 101)

print(reduce(lambda x, y: x + y, example))

# reduce in Python is like a fold-left in Ocaml

