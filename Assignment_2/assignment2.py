# author: Pongsatorn Phimnualsri

from data import capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):

    filename_check = r"^[a-zA-Z\d]{1,8}\.txt$"
    while not re.match(filename_check, filename):
        filename = input("Enter filename (1-8 letters or number, end with .txt): ")

    else:
        file = open(filename, "w")
        for country, capital in countries_capitals_dictionary.items():
            file.write(f"The capital of {country} is {capital}.\n")
        file.close()


def save_capitals():

    file = open("vowel_vowel_vowel.txt", "w")
    for capital in capitals:
        if re.search(r"[aeiouAEIOU]{3}", capital):
            file.write(f"{capital}\n")
    file.close()

    file = open("cons_cons_cons.txt", "w")
    for capital in capitals:
        if re.search(r"[^aeiouAEIOU\s]{3}", capital):
            file.write(f"{capital}\n")
    file.close()

    file = open("i_before_e.txt", "w")
    for capital in capitals:
        if re.search(r"[iI].*[eE]", capital):
            file.write(f"{capital}\n")
    file.close()

    file = open("a_a.txt", "w")
    for capital in capitals:
        if re.search(r"^[aA].*[aA]$", capital):
            file.write(f"{capital}\n")
    file.close()

    file = open("end_with_vowel.txt", "w")
    for capital in capitals:
        if re.search(r"[aeiouAEIOU]$", capital):
            file.write(f"{capital}\n")
    file.close()

    file = open("weird.txt", "w")
    for capital in capitals:
        if re.search(r"[\sxX]", capital):
            file.write(f"{capital}\n")
    file.close()

    file = open("not_start.txt", "w")
    for capital in capitals:
        if not re.search(r"^[a-eA-Ep-sP-S]", capital):
            file.write(f"{capital}\n")
    file.close()
