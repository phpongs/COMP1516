# author: Pongsatorn Phimnualsri

from data import capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    while True:
        filename = input("Enter filename (1-8 letters or number, end with .txt): ")
        if re.search(r"^[a-zA-z0-9]{1,8}.txt$", filename):
            file = open(filename, "w")
            for country, capital in countries_capitals_dictionary.items():
                file.write(f"The capital of {country} is {capital}.\n")
            file.close()
            break
        else:
            print("Try again, file name must contains 1-8 letters or number, end with .txt")


def save_capitals():

    file = open("vowel_vowel_vowel.txt", "w")
    for capital in capitals:
        if re.search(r"[aeiou]{3}", capital, re.IGNORECASE):
            file.write(f"{capital}\n")
    file.close()

    file = open("cons_cons_cons.txt", "w")
    for capital in capitals:
        if re.search(r"[bcdfghjklmnpqrstvwxyz]{3}", capital, re.IGNORECASE):
            file.write(f"{capital}\n")
    file.close()

    file = open("i_before_e.txt", "w")
    for capital in capitals:
        if re.search(r"i.*e", capital, re.IGNORECASE):
            file.write(f"{capital}\n")
    file.close()

    file = open("a_a.txt", "w")
    for capital in capitals:
        if re.search(r"^a.*a$", capital, re.IGNORECASE):
            file.write(f"{capital}\n")
    file.close()

    file = open("end_with_vowel.txt", "w")
    for capital in capitals:
        if re.search(r"[aeiou]$", capital, re.IGNORECASE):
            file.write(f"{capital}\n")
    file.close()

    file = open("weird.txt", "w")
    for capital in capitals:
        if re.search(r"['\sx]", capital, re.IGNORECASE):
            file.write(f"{capital}\n")
    file.close()

    file = open("not_start.txt", "w")
    for capital in capitals:
        if not re.search(r"^[a-ei-ps]", capital, re.IGNORECASE):
            file.write(f"{capital}\n")
    file.close()
