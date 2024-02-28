# jason wilder

countries = {"canada", "france", "china", "canada"}

if "canada" in countries:
    countries.remove("canada")
countries.add("brazil")

print(countries)

for country in countries:
    print(country, end=" ")
