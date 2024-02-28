# Author Jose Tellez

from data import countries, capitals


def get_countries(substring):
    """
    Loops through the countries tuple , finds countries that match the substring and writes them to a file
    :param substring: substring for matching as a string
    :return: None
    """
    file = open("MatchingCountries.txt", "w")

    for country in countries:
        if substring in country:
            file.write(f"{country}\n")

    file.close()


def get_capitals(substring):
    """
    Loops through the capitals tuple. If a capital contains the substring , appends the capital name to the end of the
    file
    :param substring: substring to be found as a string
    :return: None
    """
    for capital in capitals:
        if substring in capital:
            file = open("MatchingCountries.txt", "a")
            file.write(f"{capital}\n")
            file.close()


def print_file_data():
    """
    Reads the MatchingCountries.txt and loops through the resulting array , printing all lines
    :return:
    """
    file = open("MatchingCountries.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line.strip())


def main():
    get_countries("an")
    get_capitals("os")
    print_file_data()


if __name__ == '__main__':
    main()
