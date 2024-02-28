# jason wilder

countries = {"ca": ["bc", "ab", "sk"],
             "us": ["ca", "az"],
             "br": ["sp", "rj"]}

for country_code, list_of_states in countries.items():
    print(f"here are the states for {country_code}:")
    for state in list_of_states:
        print(f"\t{state}")
    print()

