# jason wilder

cars = {"mazda3": "mazda",
        "ghost": "rolls royce",
        "mustang": "ford",
        "camaro": "chevrolet",
        "f150": "ford"}

print(cars["ghost"])
print(cars["f150"])

students = {"a00123": "tiger woods",
            "a00321": "bill gates"}

countries = {"ca": "canada",
             "us": "united states of america",
             "cn": "china"}


print(countries.keys())
print(countries.values())
print(countries.items())

for k in countries.keys():
    print(f"key is {k}")

for v in countries.values():
    print(f"value is {v}")

for k, v in countries.items():
    print(f"{k} stands for {v}!")

print(type(cars))
