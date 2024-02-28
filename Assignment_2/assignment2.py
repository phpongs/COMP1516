# author: Pongsatorn Phimnualsri

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):

    def check_name():
        name_without_txt = filename[:-4]
        if len(name_without_txt) < 1 or len(name_without_txt) > 8:
            return False
        if not name_without_txt.isalnum():
            return False
        if not filename.endswith(".txt"):
            return False
        return True

    while not check_name():
        filename = input("Enter file name\n(Must contain only 1-8 letters/number)\n: ")

    with open(filename, "w") as file:
        for country, capital in countries_capitals_dictionary.items():
            file.write(f"The capital of {country} is {capital}.\n")
        file.close()


def save_capitals():
    pass
