# author: Jose Tellez, Pongs Phimnualsri, Wai Wah

from data import countries
from data import capitals


def get_countries(substring):
    """
    Loops through the countries tuple, finds countries that match the substring and writes them to a file
    :param substring: substring for matching as a string
    :return: create text file contains a country list
    """
    file = open("MatchingCountries.txt", "w")

    for country in countries:
        if substring in country:
            file.write(f"{country}\n")

    file.close()


def get_capitals(substring):
    """
    Loops through the capitals tuple. If a capital contains the substring, appends the capital name to the end of the
    file
    :param substring: substring to be found as a string
    :return: appended a capital list to an existing text file
    """
    for capital in capitals:
        if substring in capital:
            file = open("MatchingCountries.txt", "a")
            file.write(f"{capital}\n")
            file.close()


def print_file_data():
    """
    Reads the MatchingCountries.txt and loops through the resulting array, printing all lines
    :return: print result from MatchingCountries.txt
    """
    file = open("MatchingCountries.txt", "r")

    for line in file.readlines():
        print(line.strip())

    file.close()


def main():
    get_countries("an")
    get_capitals("os")
    print_file_data()


if __name__ == '__main__':
    main()
