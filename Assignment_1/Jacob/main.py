# Author: Jacob Ardelean

# importing data from the data project module
from data import countries_and_capitals, countries, capitals  # Importing data module and its variables
import project  # Importing  project module


def main():
    project.print_json_countries_and_capitals()  # Calling the function from the project module to print in JSON format

    # Looping through each letter from 'a' to 'u' for the first 3 letters of each country
    for n in range(1, 4):
        for letter in ['a', 'e', 'i', 'o', 'u']:
            print(project.get_list_of_countries_whose_nth_letter_is(n, letter))  # Printing countries

    # Looping through each letter of the alphabet and printing funny case capital cities
    for letter in map(chr, range(97, 123)):
        print(project.get_funny_case_capital_cities(letter))

    # Printing countries with doubled letters
    print(project.get_doubled_letter_countries())


if __name__ == '__main__':
    main()  # Calling the main function when the script is executed

