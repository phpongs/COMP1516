# jason wilder

cities = ['north van', 'west van', 'chilliwack', 'vancouver', 'richmond']

for city_name in cities:
    for char in city_name:
        print(char, end="   ")
    print("")

for i, v in enumerate(cities):
    print(f"city number {i} is {v}.")
