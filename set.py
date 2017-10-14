numbers = {1, 2, 3, 4, 5, 5}
print(numbers)
print(type(numbers))

animals = set(["kobuta", "tanuki", "kitsune", "neko"])
print(animals)
print(type(animals))

list_a = [1, 1, 12, 3, 3, 3, 3, 3, 3, 4]
list_b = [4, 3, 1, 12]

print(set(list_a) == set(list_b))

print(set(list_a) is set(list_b))

for element in animals:
    print(element)

animals.remove("kobuta")
print(animals)

animals.discard("saru")

#animals.remove("saru") #remove rises an error
print(animals)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setB = {2, 4, 6, 8, 10}

print(setA-setB)

print({1, 2, 3} | {2, 3, 4})
# or
print({1, 2, 3} & {2, 3, 4})
# and
print({1, 3} <= {1, 2, 3})
# subset
print(setA.union(setB))
print(setA.intersection(d setB))