# author: Pongsatorn Phimnualsri

from data import capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    Prompts the user to enter a filename adhering to specific criteria and writes a list of countries
    and their capitals to the specified file. The filename must be 1-8 letters or numbers, ending with '.txt'.
    @param filename:
    @return: none
    """
    # loop until valid filename is entered
    while True:
        filename = input("Enter filename (1-8 letters or number, end with .txt): ")
        # check if the filename matches the specific pattern
        if re.search(r"^[a-zA-z0-9]{1,8}.txt$", filename):
            file = open(filename, "w")
            # iterate over the country-capital pairs and write to the file
            for country, capital in countries_capitals_dictionary.items():
                file.write(f"The capital of {country} is {capital}.\n")
            file.close()
            break
        else:
            print("Try again, file name must contains 1-8 letters or number, end with .txt")


def save_capitals():
    """
    Writes capitals matching specific patterns to predefined files.
    Files created are based on specific patterns:
    - Containing three consecutive vowels,
    - Containing three consecutive consonants,
    - Having 'i' before 'e',
    - Starting and ending with 'a',
    - Ending with a vowel,
    - Containing a whitespace, an apostrophe, or being a single character,
    - Not starting with letters in the range 'a' to 'e' and 'i' to 'p'.
    @return: none
    """
    # define patterns and corresponding filenames
    pattern = {
        "vowel_vowel_vowel.txt": r"[aeiou]{3}",
        "cons_cons_cons.txt": r"[bcdfghjklmnpqrstvwxyz]{3}",
        "i_before_e.txt": r"i.*e",
        "a_a.txt": r"^a.*a$",
        "end_with_vowel.txt": r"[aeiou]$",
        "weird.txt": r"['\sx]",
        "not_start.txt": r"^[a-ei-ps]"
    }

    # iterate over the pattern dictionary
    for filename, pattern in pattern.items():
        file = open(filename, "w")
        # check each capital against the current pattern
        for capital in capitals:
            if re.search(pattern, capital, re.IGNORECASE):
                file.write(f"{capital}\n")
        file.close()
