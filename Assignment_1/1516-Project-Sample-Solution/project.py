
from data import countries_and_capitals, countries, capitals


def print_json_countries_and_capitals():
    """
    Prints countries and capitals in a json format
    :return: nothing
    """
    count = 0
    # Opening square bracket
    print('[')
    # Use while loops to iterate each country and capital pair, printing in json format.
    while count < len(countries_and_capitals) - 1:
        country_capital = \
            f'    {{\n'\
            f'        "country_name":"{countries_and_capitals[count][0]}",\n'\
            f'        "capital_city":"{countries_and_capitals[count][1]}"\n'\
            f'    }},'
        print(country_capital)
        count += 1

    last = countries_and_capitals[-1]
    country_capital = \
        f'    {{\n' \
        f'        "country_name":"{last[0]}",\n' \
        f'        "capital_city":"{last[1]}"\n' \
        f'    }}'
    print(country_capital)

    # Final closing square bracket
    print(']')


def get_list_of_countries_whose_nth_letter_is(n, letter):
    """
    Creates and returns a list of all countries whose nth letter matches the letter in the parameter
    Must use a for loop
    :param n: position of letter to check if it is the given letter
    :param letter: letter to check for
    :return: list of countries that have the selected letter in the selected position
    """
    letter_index = n - 1
    selected_countries = []
    for country in countries:
        if country[letter_index].lower() == letter.lower():
            selected_countries.append(country)
        else:
            pass
    return selected_countries


def get_funny_case_capital_cities(letter):
    """
    Modifies the capital cities list with strange upper case rules as follows:
    A letter that immediately precedes and follows the parameter letter is uppercased. For example, calling
    get_funny_case_capital_cities(“a”) will uppercase the previous and next letters that come before and after
    each “a” or “A” in a capital city (unless there are consecutive a’s, since every a will be lowercased).
    All other letters are lowercase. All cities that contain that letter will be stored in a list and returned.
    :param letter: letter to search for and set letters on ither side to uppercase.
    :return: modified list of cities with funny cases.
    """
    capitals_with_letter = [capital.lower() for capital in capitals if letter.lower() in capital.lower()]

    city_index = 0
    for city in capitals_with_letter:
        city_letters = list(city)
        letter_index = 0
        # Iterate through letters making upper case modifications to some letters according to the rule
        for current_letter in city_letters:
            # Assign previous letter if if the current letter is not the first one.
            if letter_index > 0:
                previous_letter = city_letters[letter_index - 1]
            else:
                previous_letter = ""

            # Assign next letter if the current letter is not the last
            if letter_index < len(city_letters) - 1:
                next_letter = city_letters[letter_index + 1]
            else:
                next_letter = ""

            # If it is the first letter, check if it matches the letter and capitalize the next letter, as long the
            # next letter is not the search letter.
            if letter_index == 0:
                if current_letter == letter and next_letter != letter:
                    city_letters[letter_index + 1] = next_letter.upper()
                else:
                    pass
            # If it is the last letter, check if it matches the search letter and capitalize the previous letter,
            # as long as it is not also the search letter.
            elif letter_index == len(city_letters) - 1:
                if current_letter == letter and previous_letter != letter:
                    city_letters[letter_index - 1] = previous_letter.upper()
                else:
                    pass
            # If it is not the first or last letter, capitalize the letters on both sides which are not also the
            # search letter
            elif current_letter == letter:
                if previous_letter != letter:
                    city_letters[letter_index - 1] = previous_letter.upper()
                if next_letter != letter:
                    city_letters[letter_index + 1] = next_letter.upper()
            else:
                pass

            # Increase letter index
            letter_index += 1
        # Set th next city value for this city with weird cases
        capitals_with_letter[city_index] = "".join(city_letters)
        # Increase the city_index
        city_index += 1
    return capitals_with_letter


def get_doubled_letter_countries():
    """
    This function creates and returns a tuple of all the countries that have consecutive repeated letters.
    :return: A tuple of countries with doubled letters, in alphabetical order by the doubled letters.
    """
    double_letter_countries = []
    # Iterate through every country to then go through the letters of each one, looking for double letters
    for country in countries:
        double_letter = ""
        letter_position = 0
        # Iterate through every letter in the country
        for letter in country:
            if letter == country[letter_position - 1]:
                double_letter = letter
            else:
                pass
            letter_position += 1

        # If a double letter was found, add the letter and country to a list item
        if double_letter != "":
            letter_country = [double_letter,country]
            double_letter_countries.append(letter_country)
        else:
            pass

    double_letter_countries.sort()  # sort by the field list items (the letter)
    country_only_list = [item[1] for item in double_letter_countries]  # Set new list after sorting to remove letters.
    return tuple(country_only_list)  # Convert to tuple


def main():
    print("I should not be called.")


if __name__ == '__main__':
    main()
