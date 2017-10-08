d1 = {'Japan': 'Tokyo', 'US': 'DC', 'Korea': 'Seoul'}

print(d1['Japan'])
#print(d1['China'])
d1['China'] = 'Beijing'
print(d1['China'])

for Country in d1.values():
    print(Country)

for Capital in d1.keys():
    print(Capital)