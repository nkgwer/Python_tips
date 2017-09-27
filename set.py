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
print(suc)
#animals.remove("saru") #remove rises an error
print(animals)

