# author: Pongsatorn Phimnualsri

from data import countries_and_capitals
from data import countries
from data import capitals


def print_json_countries_and_capitals():
    """
    prints each country and its capital in json format exactly as follows:
    [
        {
            “country_name” : “Afghanistan”,
            “capital_city” : “Kabul”
        },
        {
            “country_name” : “Albania”,
            “capital_city” : “Tirana (Tirane)”
        },
        {
            “country_name” : “Algeria”,
            “capital_city” : “Algiers”
        },
        ... etc ...
        {
            “country_name” : “Zimbabwe”,
            “capital_city” : “Harare”
        }
    ]
    :return: JSON format of countries and capitals name
    :rtype: str
    """
    i = 0                                           # index 0
    print("[")
    while i < len(countries_and_capitals):          # loops from index 0 until the end of the list
        country = (countries_and_capitals[i])[0]        # extract country from index 0 of countries_and_capitals
        capital = (countries_and_capitals[i])[1]        # extract capital from index 1 of countries_and_capitals
        if i < len(countries_and_capitals) - 1:         # If not the last item, end with a comma
            print('\t{\n\t\t“country_name” : “%s”,\n\t\t“capital_city” : “%s”\n\t},' % (country, capital))
        else:                                           # For the last item, don't end with a comma
            print('\t{\n\t\t“country_name” : “%s”,\n\t\t“capital_city” : “%s”\n\t}' % (country, capital))
        i += 1                                          # move to the next index
    print("]")


def get_list_of_countries_whose_nth_letter_is(n, letter):
    """
    creates and returns a list of all countries whose nth letter matches the letter in the parameter.
    For example, calling it as follows:
    get_list_of_countries_whose_nth_letter_is(3, “m”) would return a list of every country whose THIRD letter
    (i.e. index 2) is the letter m:
    ['Armenia', 'Cambodia', 'Cameroon', 'Comoros', 'Dominica', 'Dominican Republic', 'Gambia', 'Jamaica', 'Namibia',
     'Romania', 'Samoa', 'Somalia', 'Yemen', 'Zambia','Zimbabwe']
     Also get_list_of_countries_whose_nth_letter_is(3, “M”) would return the same list as above (in other words,
      this is case-insensitive)
    :param n: position of the letter in the country's name to match the argument letter.
    :type n: int
    :param letter: letter to match at the nth position in the country's name.
    :type letter: str
    :return: list of countries whose nth letter matches the specified letter.
    :rtype: list
    """
    countries_whose_nth_letter = []                 # empty list

    for country in countries:                       # loop through every list in "countries"
        # check if the country's name is equal or longer than "n" and if the nth letter matches the argument letter
        if len(country) >= n and country[n-1].lower() == letter.lower():
            countries_whose_nth_letter.append(country)  # if yes, add that country to the list
    return countries_whose_nth_letter


def get_funny_case_capital_cities(letter):
    """
    We know what uppercase and lowercase and titlecase and capitalize do. Now we are going to define our own letter
    casing. Here are the rules:
    A letter that immediately precedes and follows the parameter letter is uppercased. For example,
    calling get_funny_case_capital_cities(“a”) will uppercase the previous and next letters that come before and after
    each “a” or “A” in a capital city (unless there are consecutive a’s, since every a will be lowercased).
    All other letters are lowercase. All cities that contain that letter will be stored in a list and returned.
    For example:
    print(get_funny_case_capital_cities("u"))
    will return the following lists: ['kaBuL', 'LuAnda', 'BuEnos aires', 'baKu', 'nassAu', 'bRuSsels', 'thimpHu',
    'SuCre', 'OuAgadOuGOu', 'yaOuNde', 'banGuI', 'yamOuSsOuKro', 'praGuE', 'djibOuTi', 'roseAu', 'QuIto', 'SuVa',
    'banJuL', 'GuAtemala city', 'bissAu', 'port Au prince', 'teGuCigalpa', 'BuDapest', 'DuBlin', 'jeRuSalem',
    'NuR-SuLtan', 'KuWait city', 'beiRuT',
    :param letter: letter used to determine the case modification in each city name.
    :type letter: str
    :return: list of modified city names
    :rtype: list
    """
    funny_case_capital_cities = []                  # empty list

    for city in capitals:                               # loops for each list in city (city = each index)
        if letter.lower() in city.lower():              # check if there are argument "letter" in the city
            city_list = list(city)                      # convert city name to a list of character

            # nested loop
            for i in range(len(city_list)):             # loops for each list of character in "city" (i = each index)
                if city[i].lower() == letter.lower():   # check if the current character is equal to the argument letter
                    city_list[i] = city_list[i].lower() # if yes, make it lowercase
                # check if one letter BEFORE of the current character is equal to the argument letter or
                # check if one letter AFTER of the current character is equal to the argument letter
                elif (i > 0 and city_list[i - 1].lower() == letter.lower()) or (i < len(city_list) - 1 and city_list[i + 1].lower() == letter.lower()):
                    city_list[i] = city_list[i].upper() # if yes, make it uppercase
                else:
                    city_list[i] = city_list[i].lower() # otherwise, make it lowercase

            funny_city = "".join(city_list)             # convert it back to string
            funny_case_capital_cities.append(funny_city)    # add that funny city name to q list

    return funny_case_capital_cities


def get_doubled_letter_countries():
    """
    creates and returns a tuple of all the countries that have consecutive repeated letters. When called it returns that
    tuple, in alphabetical order by the doubled letters:
    ('morocco', 'greece', 'marshall islands', 'seychelles', 'cameroon', 'philippines', 'andorra', 'sierra leone',
    'guinea-bissau', 'russia', 'saint kitts and nevis')
    :return: tuple of country names that contain consecutive repeated letters, sorted by the alphabetical order of the
    first doubled letter in each name.
    :rtype: tuple
    """
    doubled_letter_with_countries = []          # empty list for store (doubled letter, country)

    for country in countries:                   # loop for each list in countries (country = each index)
        for i in range(len(country) - 1):           # loop for each list of letter in country name (i = each index)
            if country[i].lower() == country[i + 1].lower():    # check if that index == index + 1
                # if yes, add tuple contain (doubled letter, country name) into a list
                doubled_letter_with_countries.append((country[i].lower(), country))

    doubled_letter_with_countries.sort()        # sort the tuples by doubled letter

    double_letters_countries = []               # empty list for store country
    for i in doubled_letter_with_countries:     # loop for each list in double_letters_countries (i = each index)
        double_letters_countries.append(i[1])   # add index[1] (country name) to the list

    return tuple(double_letters_countries)


def main():
    """
    main function of the program
    """
    print("I should not be called")


if __name__ == '__main__':
    main()
