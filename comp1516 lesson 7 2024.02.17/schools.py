# jason wilder

bc_schools = {"bcit": "bc institute of technology",
              "ubc": "university of bc",
              "sfu": "simon fraser university"}

for school in bc_schools.keys():
    print(school.upper() + " stands for " + bc_schools[school])

for school in bc_schools.values():
    print(school.upper())

for key, school in bc_schools.items():
    print(f"{key.upper()} means {school.upper()}")
