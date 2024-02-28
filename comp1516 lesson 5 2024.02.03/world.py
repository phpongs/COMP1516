# author: jason wilder

countries = ['canada', 'ghana']
countries[0] = 'philippines'
print(countries)
countries.append("usa")
countries.insert(1, 'brazil')
countries.extend(['india', 'romania'])
countries += ['taiwan', 'colombia']
print("max is " + str(max(countries)))

if "usa" in countries:
    print(countries.index("usa"))
else:
    print("no usa")
print(type(countries))
print(len(countries))
print(countries[0])

print(countries)
