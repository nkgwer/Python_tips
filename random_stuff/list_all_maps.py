import itertools
A = range(3)
B = [True, False]
l = [[(a, b) for b in B] for a in A]
print(list(itertools.product(*l)))


def list_all_maps(range_, domain):
    map_ = [[(a, b) for b in domain] for a in range_]
    return list(itertools.product(*map_))


print(list_all_maps(['apple', 'banana', 'orange'], [True, False]))