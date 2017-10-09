uni = ['Waseda', 'Keio', 'Todai', 'Kyodai']

print(sorted(uni))
print(sorted(uni, key=lambda x: len(x)))
print(sorted(uni, key=lambda x: x[1:]))
