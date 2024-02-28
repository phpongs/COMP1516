# jason wilder

cities = ('vancouver', 'calgary')
cities_to_change = list(cities)
cities_to_change.append('burnaby')
cities = tuple(cities_to_change)

print(cities.index('vancouver'))
print(cities)

print(type(cities))


